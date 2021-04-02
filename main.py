import json
import sys
import os
import configparser

import qdarkstyle
from PyQt5 import QtWidgets, QtCore
from icmplib import ping
from PyQt5.QtCore import QThread
from PyQt5.QtWidgets import QMessageBox
from assets.chat import Ui_PartisanMain
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
        self.pushButtonRemove.clicked.connect(self.remove_contact)

    def create_new_profile(self):
        new_profile_dialog = NewProfileDialog()
        new_profile_dialog.exec_()
        print(self.currentProfile)

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
        self.update_contacts()

    def remove_contact(self):
        if self.listContacts.currentRow() > 0:
            contact_name = ((self.listContacts.item(self.listContacts.currentRow())).text())
            selected_contact = Contact(self.currentProfile)
            selected_contact.load_existing_contact(contact_name)

            confirmation_message = QMessageBox()
            confirmation_message.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
            confirmation_message.setText("Are you sure you want to delete this contact?")
            confirmation_result = confirmation_message.exec_()

            if QMessageBox.Yes == confirmation_result:
                selected_contact.remove_contact_from_database()
                self.update_contacts()

        else:
            error_dialog = QtWidgets.QErrorMessage()
            error_dialog.setWindowModality(QtCore.Qt.ApplicationModal)
            error_dialog.showMessage('This contact can\'t be removed.')
            error_dialog.exec_()

    def edit_contact(self):
        pass


def main():
    app = QtWidgets.QApplication(sys.argv)
    app.setStyleSheet(qdarkstyle.load_stylesheet())
    window = ChatWindow()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()
