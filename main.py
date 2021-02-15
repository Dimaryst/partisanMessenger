import json
import sys
import os
import configparser
import time
import qdarkstyle
from icmplib import ping

from PyQt5.QtCore import QThread
from PyQt5.QtWidgets import QMessageBox

from assets.ContactInfoDialog import Ui_DialogContactInfo
from modules.classes import User, Contact, Message
from assets.Chat import Ui_PartisanMain
from assets.AddContact import Ui_DialogAddContact
from PyQt5 import QtWidgets

from modules.server_queue import Queue


class ChatWindow(QtWidgets.QMainWindow, Ui_PartisanMain):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.account = None
        self.accountJsonPath = None
        self.active_contact = None
        # First setup
        self.centralwidget.setDisabled(True)
        self.actionAccountInfo.setDisabled(True)
        self.actionLogout.setDisabled(True)
        self.server = None
        self.check_connection_thread = CheckConnectionThread(self)
        #
        #

        self.load_session()
        self.actionAddAccount.triggered.connect(self.add_account)
        self.pushButtonAdd.clicked.connect(self.add_contact)
        self.pushButtonRemove.clicked.connect(self.remove_contact)
        self.listContacts.clicked.connect(self.active_dialog)
        self.pushButtonSendMessage.clicked.connect(self.send_message)
        self.pushButtonConfig.clicked.connect(self.contact_info)

    def listen(self):
        self.server = ServerThread(self, self.account.ip, self.account.port)
        self.server.start_server()
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
                self.listen()
            else:
                error_dialog = QtWidgets.QErrorMessage()
                error_dialog.showMessage('User file missing! Reload it manually.')
                error_dialog.exec_()

    def add_account(self):
        path_request = QtWidgets.QFileDialog
        options = QtWidgets.QFileDialog.Options()
        self.accountJsonPath, _ = path_request.getOpenFileName(self, "Select your user file...", "",
                                                               "JSON File (*.json)",
                                                               options=options)
        if self.accountJsonPath:
            # self.setWindowTitle(f"Partisan - Messenger - {self.accountJsonPath}")
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
                error_dialog.showMessage('Can\'t remove SELF!')
                error_dialog.setStyleSheet(qdarkstyle.load_stylesheet())
                error_dialog.exec_()
            else:
                contact.remove_contact(uuid)
            self.load_contact_list()
            self.listMessages.clear()

    def contact_info(self):
        # print(self.active_contact)
        if self.active_contact.contact_uuid is not None:
            info_window = EditContactDialog(self.active_contact)
            info_window.setStyleSheet(qdarkstyle.load_stylesheet())
            info_window.exec_()
            if not info_window.is_canceled:
                print("Nice")

    def active_dialog(self):
        self.check_connection_thread.quit()
        self.listMessages.clear()
        self.labelChat.setText("Chat")
        cuuid = \
            ((self.listContacts.item(self.listContacts.currentRow())).text()).split("@")[1]
        self.active_contact = Contact(self.account)
        self.active_contact.existing_contact(cuuid)
        self.labelChat.setText(f"Chat - {self.active_contact.contact_nickname}")
        for item in self.active_contact.get_messages():
            self.listMessages.addItem(item[1])
        self.listMessages.scrollToBottom()
        self.check_connection_thread.contact_ip = self.active_contact.contact_ip
        self.check_connection_thread.start()

    def send_message(self):
        if self.listContacts.currentRow() >= 0:
            self.active_contact.contact_uuid = \
                ((self.listContacts.item(self.listContacts.currentRow())).text()).split("@")[1]
            contact = Contact(self.account)
            contact.existing_contact(self.active_contact.contact_uuid)
            if self.lineInputMessage.text() != '':
                message = Message(contact, self.account)
                message.message = self.lineInputMessage.text()
                message.add_hash()
                message.save()
                message.send()
                self.listMessages.clear()
                for item in self.active_contact.get_messages():
                    self.listMessages.addItem(item[1])
                    self.listMessages.scrollToBottom()
                self.lineInputMessage.clear()
        else:
            error_dialog = QtWidgets.QErrorMessage()
            error_dialog.showMessage('Dialog is not selected')
            error_dialog.exec_()


class AddContactDialog(QtWidgets.QDialog, Ui_DialogAddContact):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.labelError.setHidden(True)
        self.is_canceled = True
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
        self.pushButtonCancel.clicked.connect(self.cancel)
        self.lineEditUsername.setText(str(self.contact.contact_nickname))
        self.lineEditUuid.setText(str(self.contact.contact_uuid))
        self.lineEditIp.setText(str(self.contact.contact_ip))
        self.lineEditPort.setText(str(self.contact.contact_port))

    def cancel(self):
        self.close()


class ServerThread(QThread):
    def __init__(self, main_window, ip, port):
        super().__init__()
        self.ip = ip
        self.port = port
        self.main_window = main_window
        self.queue = Queue(ip, port)

    def start_server(self):
        self.queue.start_server()

    def stop_server(self):
        self.queue.stop_server()

    def loop(self):
        while True:
            time.sleep(1)
            while self.queue.exists():
                self.handle(self.queue.get())

    def handle(self, message):
        try:
            # TODO: Func for incoming messages

            print("Got: {}".format(message))
            print(self)

        except Exception as e:
            print("Error: {}".format(e))


class CheckConnectionThread(QThread):
    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window
        self.contact_ip = 'localhost'

    def run(self):
        self.main_window.labelChatStatus.setText("Connection...")
        print(self.contact_ip)
        host = ping(self.contact_ip, count=5, interval=0.1, privileged=False)
        if host.is_alive:
            self.main_window.labelChatStatus.setText("Online")
        else:
            self.main_window.labelChatStatus.setText("Offline")
        self.quit()


def main():
    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    app.setStyleSheet(qdarkstyle.load_stylesheet())
    window = ChatWindow()  # Создаём объект
    window.show()  # Показываем окно
    app.exec_()  # и запускаем приложение


if __name__ == '__main__':  # Если мы запускаем файл напрямую, а не импортируем
    main()  # то запускаем функцию main()
