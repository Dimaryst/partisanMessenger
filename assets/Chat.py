# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Chat.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_PartisanMain(object):
    def setupUi(self, PartisanMain):
        PartisanMain.setObjectName("PartisanMain")
        PartisanMain.setWindowModality(QtCore.Qt.WindowModal)
        PartisanMain.resize(640, 320)
        PartisanMain.setMinimumSize(QtCore.QSize(640, 320))
        PartisanMain.setMaximumSize(QtCore.QSize(800, 600))
        self.centralwidget = QtWidgets.QWidget(PartisanMain)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.gridContacts = QtWidgets.QGridLayout()
        self.gridContacts.setObjectName("gridContacts")
        self.listContacts = QtWidgets.QListWidget(self.centralwidget)
        self.listContacts.setStyleSheet("")
        self.listContacts.setObjectName("listContacts")
        self.gridContacts.addWidget(self.listContacts, 3, 0, 1, 2)
        self.pushButtonAdd = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonAdd.setObjectName("pushButtonAdd")
        self.gridContacts.addWidget(self.pushButtonAdd, 2, 0, 1, 1)
        self.pushButtonRemove = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonRemove.setObjectName("pushButtonRemove")
        self.gridContacts.addWidget(self.pushButtonRemove, 2, 1, 1, 1)
        self.labelContactList = QtWidgets.QLabel(self.centralwidget)
        self.labelContactList.setObjectName("labelContactList")
        self.gridContacts.addWidget(self.labelContactList, 0, 0, 1, 2)
        self.lineContacts = QtWidgets.QFrame(self.centralwidget)
        self.lineContacts.setFrameShape(QtWidgets.QFrame.HLine)
        self.lineContacts.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.lineContacts.setObjectName("lineContacts")
        self.gridContacts.addWidget(self.lineContacts, 1, 0, 1, 2)
        self.horizontalLayout.addLayout(self.gridContacts)
        self.gridChat = QtWidgets.QGridLayout()
        self.gridChat.setObjectName("gridChat")
        self.listMessages = QtWidgets.QListWidget(self.centralwidget)
        self.listMessages.setObjectName("listMessages")
        self.gridChat.addWidget(self.listMessages, 3, 0, 1, 2)
        self.pushButtonSendMessage = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonSendMessage.setObjectName("pushButtonSendMessage")
        self.gridChat.addWidget(self.pushButtonSendMessage, 5, 1, 1, 1)
        self.lineInputMessage = QtWidgets.QLineEdit(self.centralwidget)
        self.lineInputMessage.setInputMask("")
        self.lineInputMessage.setText("")
        self.lineInputMessage.setObjectName("lineInputMessage")
        self.gridChat.addWidget(self.lineInputMessage, 5, 0, 1, 1)
        self.lineChat = QtWidgets.QFrame(self.centralwidget)
        self.lineChat.setFrameShape(QtWidgets.QFrame.HLine)
        self.lineChat.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.lineChat.setObjectName("lineChat")
        self.gridChat.addWidget(self.lineChat, 1, 0, 1, 2)
        self.labelChat = QtWidgets.QLabel(self.centralwidget)
        self.labelChat.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.labelChat.setObjectName("labelChat")
        self.gridChat.addWidget(self.labelChat, 0, 0, 1, 2)
        self.pushButtonConfig = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonConfig.setObjectName("pushButtonConfig")
        self.gridChat.addWidget(self.pushButtonConfig, 2, 0, 1, 2)
        self.horizontalLayout.addLayout(self.gridChat)
        PartisanMain.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(PartisanMain)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 640, 24))
        self.menubar.setObjectName("menubar")
        self.menuAccount = QtWidgets.QMenu(self.menubar)
        self.menuAccount.setObjectName("menuAccount")
        PartisanMain.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(PartisanMain)
        self.statusbar.setObjectName("statusbar")
        PartisanMain.setStatusBar(self.statusbar)
        self.actionAddAccount = QtWidgets.QAction(PartisanMain)
        self.actionAddAccount.setObjectName("actionAddAccount")
        self.actionAccountInfo = QtWidgets.QAction(PartisanMain)
        self.actionAccountInfo.setObjectName("actionAccountInfo")
        self.actionLogout = QtWidgets.QAction(PartisanMain)
        self.actionLogout.setObjectName("actionLogout")
        self.menuAccount.addAction(self.actionAddAccount)
        self.menuAccount.addAction(self.actionAccountInfo)
        self.menuAccount.addAction(self.actionLogout)
        self.menubar.addAction(self.menuAccount.menuAction())

        self.retranslateUi(PartisanMain)
        QtCore.QMetaObject.connectSlotsByName(PartisanMain)

    def retranslateUi(self, PartisanMain):
        _translate = QtCore.QCoreApplication.translate
        PartisanMain.setWindowTitle(_translate("PartisanMain", "Partisan - Messenger"))
        self.pushButtonAdd.setText(_translate("PartisanMain", "Add"))
        self.pushButtonRemove.setText(_translate("PartisanMain", "Remove"))
        self.labelContactList.setText(_translate("PartisanMain", "Contact List"))
        self.pushButtonSendMessage.setText(_translate("PartisanMain", "Send"))
        self.lineInputMessage.setPlaceholderText(_translate("PartisanMain", "Type your message here..."))
        self.labelChat.setText(_translate("PartisanMain", "Chat"))
        self.pushButtonConfig.setText(_translate("PartisanMain", "Chat Configuration"))
        self.menuAccount.setTitle(_translate("PartisanMain", "Account"))
        self.actionAddAccount.setText(_translate("PartisanMain", "Add Account..."))
        self.actionAccountInfo.setText(_translate("PartisanMain", "Account Info"))
        self.actionLogout.setText(_translate("PartisanMain", "Logout"))