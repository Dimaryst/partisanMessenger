import os

from PyQt5 import QtWidgets, QtCore
from PyQt5.QtCore import QRegExp
from PyQt5.QtGui import QRegExpValidator

from assets.newProfile import Ui_DialogNewProfile
from assets.newContact import Ui_DialogNewContact
from modules.classes import Profile, Contact


class NewProfileDialog(QtWidgets.QDialog, Ui_DialogNewProfile):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.is_canceled = True
        self.labelError.setHidden(True)
        self.pushButtonCreate.clicked.connect(self.create_profile)
        self.pushButtonCancel.clicked.connect(self.cancel)

        rx_ipv6 = QRegExp("([0-9a-fA-F]{0,4}\:[0-9a-fA-F]{0,4}\:"
                          "[0-9a-fA-F]{0,4}\:[0-9a-fA-F]{0,4}\:"
                          "[0-9a-fA-F]{0,4}\:[0-9a-fA-F]{0,4}\:"
                          "[0-9a-fA-F]{0,4}\:[0-9a-fA-F]{0,4})")

        self.lineEditIp.setValidator(QRegExpValidator(rx_ipv6))

    def create_profile(self):
        if not os.path.exists("profile"):
            os.mkdir("profile")
        print(f"New profile IP: {self.lineEditIp.text()}")
        new_profile = Profile(self.lineEditIp.text())
        new_profile.new_contact_list()
        self.is_canceled = False
        self.close()

    def cancel(self):
        self.close()


class NewContactDialog(QtWidgets.QDialog, Ui_DialogNewContact):
    def __init__(self, main_window):
        super().__init__()
        self.setupUi(self)
        self.main_window = main_window
        self.is_canceled = True

        #
        rx_name = QRegExp('\w{0,16}')
        rx_ipv6 = QRegExp("([0-9a-fA-F]{0,4}\:[0-9a-fA-F]{0,4}\:"
                          "[0-9a-fA-F]{0,4}\:[0-9a-fA-F]{0,4}\:"
                          "[0-9a-fA-F]{0,4}\:[0-9a-fA-F]{0,4}\:"
                          "[0-9a-fA-F]{0,4}\:[0-9a-fA-F]{0,4})")

        self.lineEditIp.setValidator(QRegExpValidator(rx_ipv6))
        self.lineEditName.setValidator(QRegExpValidator(rx_name))

        self.labelError.setHidden(True)
        self.newContact = Contact(self.main_window.currentProfile)
        self.pushButtonAdd.clicked.connect(self.add_new_contact)
        self.pushButtonCancel.clicked.connect(self.cancel)

    def add_new_contact(self):
        if self.newContact.is_exist_name(self.lineEditName.text()) or \
                self.newContact.is_exist_ip(self.lineEditIp.text()):
            error_dialog = QtWidgets.QErrorMessage()
            error_dialog.setWindowModality(QtCore.Qt.ApplicationModal)
            error_dialog.showMessage('This name or IP is already in use!')
            error_dialog.exec_()
        elif self.lineEditIp.text() == "" or self.lineEditName.text() == "":
            error_dialog = QtWidgets.QErrorMessage()
            error_dialog.setWindowModality(QtCore.Qt.ApplicationModal)
            error_dialog.showMessage('Fields can\'t be empty!')
            error_dialog.exec_()
        else:
            self.newContact.set_ip(self.lineEditIp.text())
            self.newContact.set_name(self.lineEditName.text())
            self.newContact.add_contact_to_database()
            self.close()

    def cancel(self):
        self.close()
