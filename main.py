import json
import sys
import os
import configparser

import qdarkstyle
from PyQt5 import QtWidgets
from icmplib import ping
from PyQt5.QtCore import QThread
from PyQt5.QtWidgets import QMessageBox
from assets.chat import Ui_PartisanMain
from assets.newProfile import Ui_DialogNewProfile
from modules.classes import Profile
from modules.server import Server


class ChatWindow(QtWidgets.QMainWindow, Ui_PartisanMain):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        #
        self.currentProfile = None
        self.currentProfileDatabasePath = None

        # Events
        self.actionCreateNewProfile.triggered.connect(self.create_new_profile)
        self.actionLoadProfile.triggered.connect(self.load_profile)

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
            pass


class NewProfileDialog(QtWidgets.QDialog, Ui_DialogNewProfile):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.is_canceled = True
        self.labelError.setHidden(True)
        self.pushButtonCreate.clicked.connect(self.create_profile)
        self.pushButtonCancel.clicked.connect(self.cancel)

    def create_profile(self):
        if not os.path.exists("profile"):
            os.mkdir("profile")
        print(f"New profile IP: {self.lineEditIp.text()}")
        new_profile = Profile(self.lineEditIp.text())
        new_profile.new_contact_list()
        self.close()

    def cancel(self):
        self.close()


def main():
    app = QtWidgets.QApplication(sys.argv)
    app.setStyleSheet(qdarkstyle.load_stylesheet())
    window = ChatWindow()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()
