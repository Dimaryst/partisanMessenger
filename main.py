import json
import sys
import os
import configparser

import qdarkstyle
from PyQt5 import QtWidgets
from icmplib import ping
from PyQt5.QtCore import QThread
from PyQt5.QtWidgets import QMessageBox
from assets.chatLite import Ui_PartisanMain
from assets.newUserDialog import Ui_DialogNewUser
from modules.server import Server


class ChatWindow(QtWidgets.QMainWindow, Ui_PartisanMain):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.myIp = None

    def connectionAction(self):
        pass


class NewUserDialog(QtWidgets.QDialog, Ui_DialogNewUser):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.is_canceled = True
        self.labelError.setHidden(True)
        self.pushButtonCreate.clicked.connect(self.create_account)
        self.pushButtonCancel.clicked.connect(self.cancel)

    def create_account(self):
        #
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
