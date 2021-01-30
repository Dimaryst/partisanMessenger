# This is a sample Python script.

import os
import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QPushButton, QAction, QLineEdit, QMessageBox, QLabel, QGridLayout, QDesktopWidget
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot

class App(QMainWindow):

    def __init__(self):
        super().__init__()
        self.title = 'Grant sudo access'
        self.left = 100
        self.top = 100
        self.width = 400
        self.height = 100
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.setFixedSize(320, 100)

        # Create textbox
        self.textbox = QLineEdit(self)
        self.textbox.move(10, 15)
        self.textbox.resize(300, 30)

        # Create a button in the window
        self.grant_button = QPushButton('Grant', self)
        self.grant_button.move(20, 60)
        self.grant_button.clicked.connect(self.on_click_grant)

        self.abort_button = QPushButton('Abort', self)
        self.abort_button.move(200, 60)
        self.abort_button.clicked.connect(self.on_click_abort)

        self.show()

    @pyqtSlot()
    def on_click_grant(self):
        print(self.textbox.text())
        sys.exit()

    def on_click_abort(self):
        sys.exit()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    # app = QtWidgets.QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
    # sys.exit()
