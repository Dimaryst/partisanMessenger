import json
import sys
import os
import configparser

import qdarkstyle
from icmplib import ping

from PyQt5.QtCore import QThread
from PyQt5.QtWidgets import QMessageBox

from assets.ContactInfoDialog import Ui_DialogContactInfo
from assets.Chat import Ui_PartisanMain
from assets.AddContact import Ui_DialogAddContact
from assets.NewAccountDialog import Ui_DialogNewAccount

from modules.classes import User, Contact, Message
from modules.server import is_valid_ipv6_address, is_valid_ipv4_address
from PyQt5 import QtWidgets

from modules.server import Server


class ChatWindow(QtWidgets.QMainWindow, Ui_PartisanMain):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.account = None
        self.accountJsonPath = None
        self.active_contact = None
        self.centralwidget.setDisabled(True)
        self.actionAccountInfo.setDisabled(True)
        self.actionConnection.setText("Connection: Offline")
        self.lineInputMessage.setMaxLength(48)
        # Threads
        self.check_connection_thread = CheckConnectionThread(self)  # Thread ping selected contact
        self.messages_server_thread = MessagesServerThread(self, 'localhost', 7045)  # Incoming messages server
        #
        self.actionAddAccount.triggered.connect(self.add_account)
        self.actionNew.triggered.connect(self.new_account)
        self.listContacts.clicked.connect(self.active_dialog)

        self.pushButtonAdd.clicked.connect(self.add_contact)
        self.pushButtonRemove.clicked.connect(self.remove_contact)
        self.pushButtonClearChat.clicked.connect(self.clear_chat)
        self.pushButtonSendMessage.clicked.connect(self.send_message)
        self.pushButtonConfig.clicked.connect(self.contact_info)
        self.pushButtonUpdateListMessages.clicked.connect(self.update_messages_list)
        self.load_session()  # Load user from config and json

    def listen(self):
        self.messages_server_thread.ip = self.account.ip
        self.messages_server_thread.port = self.account.port
        self.messages_server_thread.start()
        self.actionConnection.setText("Connection: OK")

    def load_session(self):
        if os.path.exists('config.ini'):
            config = configparser.ConfigParser()
            config.read("config.ini")
            user = config["Session"]["user"]
            if os.path.exists(f"user/{user}.json"):
                with open(f"user/{user}.json", 'r') as account_file:
                    card = json.load(account_file)
                    # self.setWindowTitle(f"Partisan - Messenger - user/{user}.json")
                self.account = User()
                self.active_contact = Contact(self.account)
                self.account.uuid, self.account.ip, self.account.port = \
                    card['UUID'], card['IP'], card['PORT']
                self.centralwidget.setEnabled(True)
                self.load_contact_list()
                self.actionAddAccount.setDisabled(True)
                self.lineInputMessage.setDisabled(True)
                self.listen()
            else:
                error_dialog = QtWidgets.QErrorMessage()
                error_dialog.showMessage('User file missing! Reload it manually.')
                error_dialog.exec_()
        else:
            error_dialog = QtWidgets.QErrorMessage()
            error_dialog.showMessage('Config file does not exist!')
            error_dialog.exec_()

    def new_account(self):
        new_account_form = NewAccountDialog()
        new_account_form.exec_()
        if not new_account_form.is_canceled:
            self.load_session()

    def add_account(self):
        path_request = QtWidgets.QFileDialog
        options = QtWidgets.QFileDialog.Options()
        self.accountJsonPath, _ = path_request.getOpenFileName(self, "Select your user file...", "",
                                                               "JSON File (*.json)",
                                                               options=options)
        if self.accountJsonPath:
            self.centralwidget.setEnabled(True)
            with open(self.accountJsonPath, 'r') as account_file:
                card = json.load(account_file)
            self.account = User()
            self.active_contact = Contact(self.account)
            self.account.uuid, self.account.ip, self.account.port = \
                card['UUID'], card['IP'], card['PORT']
            self.centralwidget.setEnabled(True)
            self.load_contact_list()
            with open('config.ini', 'w') as config_file:
                config_file.write(f"[Session]\nuser={self.account.uuid}")
            self.actionAddAccount.setDisabled(True)
            self.listen()

    def load_contact_list(self):
        self.listContacts.clear()
        for item in self.account.get_contacts():
            self.listContacts.addItem(f"{item[1]}\n@{item[2]}")

    def add_contact(self):
        add_contact_window = AddContactDialog()
        add_contact_window.setStyleSheet(qdarkstyle.load_stylesheet())
        add_contact_window.exec_()
        if not add_contact_window.is_canceled:
            new_contact = Contact(self.account)
            new_contact.contact_nickname = add_contact_window.lineNickname.text()
            new_contact.contact_uuid = add_contact_window.lineNewContactUuid.text()
            new_contact.contact_ip = add_contact_window.lineNewContactIp.text()
            new_contact.contact_port = add_contact_window.lineNewContactPort.text()
            new_contact.add_contact()
            self.load_contact_list()

    def remove_contact(self):
        confirmation_message = QMessageBox()
        confirmation_message.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        confirmation_message.setText("Are you sure you want to delete this contact?")
        confirmation_result = confirmation_message.exec_()
        if QMessageBox.Yes == confirmation_result:
            uuid = ((self.listContacts.item(self.listContacts.currentRow())).text()).split("@")[1]
            contact = Contact(self.account)
            if uuid == self.account.uuid:
                error_dialog = QtWidgets.QErrorMessage()
                error_dialog.showMessage('Can\'t remove self!')
                error_dialog.setStyleSheet(qdarkstyle.load_stylesheet())
                error_dialog.exec_()
            else:
                contact.remove_contact(uuid)
            self.load_contact_list()
            self.listMessages.clear()

    def contact_info(self):
        if self.active_contact.contact_uuid is not None:
            info_window = EditContactDialog(self.active_contact)
            info_window.setStyleSheet(qdarkstyle.load_stylesheet())
            info_window.exec_()
            if not info_window.is_canceled:
                print("Nice")

    def active_dialog(self):
        if self.check_connection_thread.isRunning():
            # self.check_connection_thread.quit()
            self.check_connection_thread.terminate()
        self.update_active_contact()
        self.update_messages_list()
        self.pushButtonSendMessage.setDisabled(True)
        self.lineInputMessage.clear()
        self.check_connection_thread.contact_ip = self.active_contact.contact_ip
        self.check_connection_thread.start()
        self.update_messages_list()

    def send_message(self):
        if self.listContacts.currentRow() >= 1:
            self.update_active_contact()
            if self.lineInputMessage.text() != '':
                message = Message(self.active_contact, self.account)
                message.message = self.lineInputMessage.text()
                message.add_hash()
                message.save()
                message.send()
                self.lineInputMessage.clear()
                self.update_messages_list()
        elif self.listContacts.currentRow() == 0:
            self.update_active_contact()
            message = Message(self.active_contact, self.account)
            message.message = self.lineInputMessage.text()
            message.save()
            self.lineInputMessage.clear()
            self.update_messages_list()
        else:
            error_dialog = QtWidgets.QErrorMessage()
            error_dialog.showMessage('Dialog is not selected')
            error_dialog.exec_()

    def update_messages_list(self):
        if self.listContacts.currentRow() >= 0:
            self.update_active_contact()
            self.listMessages.clear()
            for item in self.active_contact.get_messages():
                self.listMessages.addItem(item[1])
                self.listMessages.scrollToBottom()

    def update_active_contact(self):
        if self.listContacts.currentRow() >= 0:
            cuuid = \
                ((self.listContacts.item(self.listContacts.currentRow())).text()).split("@")[1]  # Selected UUID
            self.active_contact = Contact(self.account)  # Update current Contact Obj
            self.active_contact.existing_contact(cuuid)  # and load contact info via selected UUID
            self.labelChat.setText(f"Chat - {self.active_contact.contact_nickname}")
            # self.labelChatStatus.setText("Waiting...")

    def clear_chat(self):
        self.update_active_contact()
        warning_dialog = QtWidgets.QMessageBox
        answer = warning_dialog.question(self, '', "Are you sure to delete all messages?",
                                         warning_dialog.Yes | warning_dialog.No)
        if answer == warning_dialog.Yes:
            self.active_contact.delete_messages()
            self.update_messages_list()


class AddContactDialog(QtWidgets.QDialog, Ui_DialogAddContact):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.labelError.setHidden(True)
        self.is_canceled = True
        self.lineNickname.setMaxLength(12)
        self.lineNewContactPort.setMaxLength(5)
        self.pushButtonAdd.clicked.connect(self.add_contact)
        self.pushButtonCancel.clicked.connect(self.cancel)

    def add_contact(self):
        if (self.lineNickname.text() == '') \
                or (self.lineNewContactUuid.text() == '') \
                or (self.lineNewContactIp.text() == '') \
                or (self.lineNewContactPort.text() == ''):
            self.labelError.setHidden(False)
            self.labelError.setText("Fields can't be empty")
        else:
            self.is_canceled = False
            self.close()

    def cancel(self):
        self.close()


class EditContactDialog(QtWidgets.QDialog, Ui_DialogContactInfo):
    def __init__(self, contact):
        super().__init__()
        self.setupUi(self)
        self.labelError.setHidden(True)
        self.is_canceled = True
        self.contact = contact
        self.lineEditUuid.setReadOnly(True)
        self.pushButtonCancel.clicked.connect(self.cancel)
        self.lineEditUsername.setText(str(self.contact.contact_nickname))
        self.lineEditUuid.setText(str(self.contact.contact_uuid))
        self.lineEditIp.setText(str(self.contact.contact_ip))
        self.lineEditPort.setText(str(self.contact.contact_port))

    def cancel(self):
        self.close()


class NewAccountDialog(QtWidgets.QDialog, Ui_DialogNewAccount):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.is_canceled = True
        self.labelError.setHidden(True)
        self.lineEditUsername.setMaxLength(12)
        self.lineEditPort.setMaxLength(5)
        self.lineEditPort.setText("7529")
        self.pushButtonCreate.clicked.connect(self.create_account)
        self.pushButtonCancel.clicked.connect(self.cancel)

    def check_password(self):
        if self.lineEditPassword.text() == self.lineEditPasswordRepeat.text():
            return True
        else:
            return False

    def create_account(self):
        if (self.lineEditUsername.text() == '') \
                or (self.lineEditIp.text() == '') \
                or (self.lineEditPort.text() == ''):
            self.labelError.setHidden(False)
            self.labelError.setText("Fields can't be empty")
        elif not self.check_password():
            self.labelError.setHidden(False)
            self.labelError.setText("Check password")
        elif os.path.exists('user'):
            error_dialog = QtWidgets.QErrorMessage()
            error_dialog.setModal(True)
            error_dialog.showMessage('Folder \'user\' already exist!\n'
                                     'Add your user card manually or remove folder \'user\' and try again.')
            error_dialog.exec_()
            self.close()
        else:
            os.mkdir('user')
            os.mkdir('user/dialogs')
            New = User()
            New.new_user(self.lineEditIp.text())
            New.set_name(self.lineEditUsername.text())
            New.port = self.lineEditPort.text()
            print(f"New user:\n{New.ip}:{New.port}\nID: {New.uuid}")
            with open('config.ini', 'w') as config_file:
                config_file.write(f"[Session]\nuser={New.uuid}")
            info_message = QtWidgets.QMessageBox()
            info_message.setModal(True)
            info_message.setText('Account has been successfully created.')
            info_message.exec_()

            self.is_canceled = False
            self.close()

    def cancel(self):
        self.close()


class CheckConnectionThread(QThread):
    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window
        self.contact_ip = 'localhost'

    def run(self):
        if is_valid_ipv4_address(self.contact_ip) \
                or is_valid_ipv6_address(self.contact_ip) \
                or self.contact_ip == "localhost":
            self.main_window.labelChatStatus.setText("Connection...")
            host = ping(self.contact_ip, count=5, interval=0.1, privileged=False)
            if host.is_alive:
                self.main_window.labelChatStatus.setText("Yggdrasil Online")
                self.main_window.pushButtonSendMessage.setEnabled(True)
                self.main_window.lineInputMessage.setEnabled(True)
            else:
                self.main_window.labelChatStatus.setText("Yggdrasil Offline")
            self.quit()
            # self.terminate()

        else:
            print(self.contact_ip)
            self.main_window.labelChatStatus.setText("Invalid Address/Port")


class MessagesServer(Server):
    def handle(self, message):
        print(message.decode('utf-8'))
        package = json.loads(message.decode('utf-8'))
        # Load Current User as obj
        config = configparser.ConfigParser()
        config.read("config.ini")
        user = config["Session"]["user"]
        with open(f"user/{user}.json", 'r') as account_file:
            card = json.load(account_file)

        receiver = User()  # Current User (same as in ChatWindow)
        receiver.uuid, receiver.ip, receiver.port = card['UUID'], card['IP'], card['PORT']

        sender = Contact(receiver)

        print("Sender in contact list:", sender.is_exist(package[0]))
        if sender.is_exist(package[0]) and receiver.uuid == package[1]:
            sender.existing_contact(package[0])
            message = Message(receiver, sender)
            message.load(package)
            message.receive()


class MessagesServerThread(QThread):
    def __init__(self, main_window, ip, port):
        super().__init__()
        self.main_window = main_window
        self.ip = ip
        self.port = port

    def run(self):
        if is_valid_ipv4_address(self.ip) or is_valid_ipv6_address(self.ip) or self.ip == "localhost":
            if 1024 <= self.port <= 65536:
                server = MessagesServer(self.ip, self.port)
                server.start_server()
                server.loop()
                server.stop_server()
            else:
                self.main_window.actionConnection.setText("Connection: Bad Port")
                self.quit()
        else:
            self.main_window.actionConnection.setText("Connection: Bad IP")
            self.quit()


def main():
    app = QtWidgets.QApplication(sys.argv)
    app.setStyleSheet(qdarkstyle.load_stylesheet())
    window = ChatWindow()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()
