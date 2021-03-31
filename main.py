import json
import sys
import os
import configparser

import qdarkstyle
from PyQt5 import QtWidgets
from icmplib import ping
from PyQt5.QtCore import QThread
from PyQt5.QtWidgets import QMessageBox
import modules.classes
from assets.chat import Ui_PartisanMain
from assets.newProfile import Ui_DialogNewProfile
from assets.newContact import Ui_DialogNewContact
from modules.classes import Profile, Contact
from modules.dialogs import NewProfileDialog, NewContactDialog
from modules.server import Server


class ChatWindow(QtWidgets.QMainWindow, Ui_PartisanMain):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        #
        self.currentProfile = None
        self.currentProfileDatabasePath = None
        self.centralwidget.setDisabled(True)

        # Events
        self.actionCreateNewProfile.triggered.connect(self.create_new_profile)
        self.actionLoadProfile.triggered.connect(self.load_profile)
        self.pushButtonAdd.clicked.connect(self.add_new_contact)

    def create_new_profile(self):
        new_profile_dialog = NewProfileDialog()
        new_profile_dialog.exec_()
        if not new_profile_dialog.is_canceled:
            print(f"Profile updated: {self.currentProfile.get_profile_ip()}")

    def load_profile(self):
        profile_database_path_request = QtWidgets.QFileDialog
        options = QtWidgets.QFileDialog.Options()

        self.currentProfileDatabasePath, _ = \
            profile_database_path_request.getOpenFileName(self, "Select profile database...", "",
                                                          "Database File (*.db)",
                                                          options=options)
        if self.currentProfileDatabasePath:
            self.currentProfile = Profile.get_existing_profile(self.currentProfileDatabasePath)
            print(self.currentProfile.get_profile_ip())
            self.update_contacts()
            self.centralwidget.setEnabled(True)

    def update_contacts(self):
        if self.currentProfile is not None:
            self.listContacts.clear()
            for contact in self.currentProfile.get_contacts():
                self.listContacts.addItem(contact[2])

    def add_new_contact(self):
        add_new_contact_dialog = NewContactDialog(self)
        add_new_contact_dialog.exec_()
        if not add_new_contact_dialog.is_canceled:
            print(add_new_contact_dialog.lineEditIp.text())
            self.update_contacts()


def main():
    app = QtWidgets.QApplication(sys.argv)
    app.setStyleSheet(qdarkstyle.load_stylesheet())
    window = ChatWindow()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()
