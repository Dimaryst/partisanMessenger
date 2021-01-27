import json
import sys
import os
from PyQt5.QtWidgets import QMessageBox

from modules.classes import User, Contact, Message
from assets.Chat import Ui_PartisanMain
from assets.AddContact import Ui_DialogAddContact
from PyQt5 import QtWidgets


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

        #
        #

        self.actionAddAccount.triggered.connect(self.add_account)
        self.pushButtonAdd.clicked.connect(self.add_contact)
        self.pushButtonRemove.clicked.connect(self.remove_contact)
        self.listContacts.clicked.connect(self.active_dialog)
        self.pushButtonSendMessage.clicked.connect(self.send_message)

    def add_account(self):
        path_request = QtWidgets.QFileDialog
        options = QtWidgets.QFileDialog.Options()
        self.accountJsonPath, _ = path_request.getOpenFileName(self, "Select your user file...", "",
                                                               "JSON File (*.json)",
                                                               options=options)
        if self.accountJsonPath:
            self.setWindowTitle(f"Partisan - Messenger - {self.accountJsonPath}")
            self.centralwidget.setEnabled(True)
            with open(self.accountJsonPath, 'r') as account_file:
                card = json.load(account_file)
            self.account = User()
            self.active_contact = Contact(self.account)
            self.account.uuid, self.account.ip, self.account.port = \
                card['UUID'], card['IP'], card['PORT']
            self.centralwidget.setEnabled(True)
            self.load_contact_list()

    def load_contact_list(self):
        self.listContacts.clear()
        for item in self.account.get_contacts():
            self.listContacts.addItem(f"{item[1]}\n@{item[2]}")

    def add_contact(self):
        add_contact_window = AddContactDialog()
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
                error_dialog.exec_()
            else:
                contact.remove_contact(uuid)
            self.load_contact_list()

    def active_dialog(self):
        self.active_contact.contact_uuid = \
            ((self.listContacts.item(self.listContacts.currentRow())).text()).split("@")[1]
        self.active_contact.contact_nickname = \
            ((self.listContacts.item(self.listContacts.currentRow())).text()).split("@")[0]
        self.labelChat.setText(f"Chat - {self.active_contact.contact_nickname}@{self.active_contact.contact_uuid}")
        self.listMessages.clear()
        for item in self.active_contact.get_messages():
            self.listMessages.addItem(item[1])
        self.listMessages.scrollToBottom()

    def send_message(self):
        if self.listContacts.currentRow() >= 0:
            self.active_contact.contact_uuid = \
                ((self.listContacts.item(self.listContacts.currentRow())).text()).split("@")[1]
            contact = Contact(self.account)
            contact.existing_contact(self.active_contact.contact_uuid)
            if self.lineInputMessage.text() != '':
                message = Message(contact)
                message.message = "ME -> " + self.lineInputMessage.text()
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


def main():
    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    window = ChatWindow()  # Создаём объект
    window.show()  # Показываем окно
    app.exec_()  # и запускаем приложение


if __name__ == '__main__':  # Если мы запускаем файл напрямую, а не импортируем
    main()  # то запускаем функцию main()
