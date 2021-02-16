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
        PartisanMain.resize(1055, 600)
        PartisanMain.setMinimumSize(QtCore.QSize(900, 600))
        PartisanMain.setMaximumSize(QtCore.QSize(1920, 1080))
        self.centralwidget = QtWidgets.QWidget(PartisanMain)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.gridContacts = QtWidgets.QGridLayout()
        self.gridContacts.setObjectName("gridContacts")
        self.labelContactList = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelContactList.sizePolicy().hasHeightForWidth())
        self.labelContactList.setSizePolicy(sizePolicy)
        self.labelContactList.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse)
        self.labelContactList.setObjectName("labelContactList")
        self.gridContacts.addWidget(self.labelContactList, 0, 0, 1, 2)
        self.listContacts = QtWidgets.QListWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.listContacts.sizePolicy().hasHeightForWidth())
        self.listContacts.setSizePolicy(sizePolicy)
        self.listContacts.setMinimumSize(QtCore.QSize(0, 0))
        self.listContacts.setMaximumSize(QtCore.QSize(200, 16777215))
        self.listContacts.setStyleSheet("")
        self.listContacts.setObjectName("listContacts")
        self.gridContacts.addWidget(self.listContacts, 2, 0, 1, 2)
        self.pushButtonRemove = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButtonRemove.sizePolicy().hasHeightForWidth())
        self.pushButtonRemove.setSizePolicy(sizePolicy)
        self.pushButtonRemove.setObjectName("pushButtonRemove")
        self.gridContacts.addWidget(self.pushButtonRemove, 1, 1, 1, 1)
        self.pushButtonAdd = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButtonAdd.sizePolicy().hasHeightForWidth())
        self.pushButtonAdd.setSizePolicy(sizePolicy)
        self.pushButtonAdd.setObjectName("pushButtonAdd")
        self.gridContacts.addWidget(self.pushButtonAdd, 1, 0, 1, 1)
        self.horizontalLayout.addLayout(self.gridContacts)
        self.lineChat = QtWidgets.QFrame(self.centralwidget)
        self.lineChat.setFrameShape(QtWidgets.QFrame.VLine)
        self.lineChat.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.lineChat.setObjectName("lineChat")
        self.horizontalLayout.addWidget(self.lineChat)
        self.verticalLayoutChat = QtWidgets.QVBoxLayout()
        self.verticalLayoutChat.setObjectName("verticalLayoutChat")
        self.listMessages = QtWidgets.QListWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.listMessages.sizePolicy().hasHeightForWidth())
        self.listMessages.setSizePolicy(sizePolicy)
        self.listMessages.setObjectName("listMessages")
        self.verticalLayoutChat.addWidget(self.listMessages)
        self.horizontalLayoutMessageInputAndButton = QtWidgets.QHBoxLayout()
        self.horizontalLayoutMessageInputAndButton.setObjectName("horizontalLayoutMessageInputAndButton")
        self.lineInputMessage = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineInputMessage.sizePolicy().hasHeightForWidth())
        self.lineInputMessage.setSizePolicy(sizePolicy)
        self.lineInputMessage.setInputMask("")
        self.lineInputMessage.setText("")
        self.lineInputMessage.setObjectName("lineInputMessage")
        self.horizontalLayoutMessageInputAndButton.addWidget(self.lineInputMessage)
        self.pushButtonSendMessage = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonSendMessage.setDefault(True)
        self.pushButtonSendMessage.setObjectName("pushButtonSendMessage")
        self.horizontalLayoutMessageInputAndButton.addWidget(self.pushButtonSendMessage)
        self.verticalLayoutChat.addLayout(self.horizontalLayoutMessageInputAndButton)
        self.horizontalLayout.addLayout(self.verticalLayoutChat)
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.horizontalLayout.addWidget(self.line)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.labelChat = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelChat.sizePolicy().hasHeightForWidth())
        self.labelChat.setSizePolicy(sizePolicy)
        self.labelChat.setMinimumSize(QtCore.QSize(140, 0))
        self.labelChat.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.labelChat.setObjectName("labelChat")
        self.verticalLayout.addWidget(self.labelChat)
        self.labelChatStatus = QtWidgets.QLabel(self.centralwidget)
        self.labelChatStatus.setText("")
        self.labelChatStatus.setObjectName("labelChatStatus")
        self.verticalLayout.addWidget(self.labelChatStatus)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.pushButtonConfig = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButtonConfig.sizePolicy().hasHeightForWidth())
        self.pushButtonConfig.setSizePolicy(sizePolicy)
        self.pushButtonConfig.setMinimumSize(QtCore.QSize(0, 0))
        self.pushButtonConfig.setObjectName("pushButtonConfig")
        self.verticalLayout.addWidget(self.pushButtonConfig)
        self.horizontalLayout.addLayout(self.verticalLayout)
        PartisanMain.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(PartisanMain)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1055, 24))
        self.menubar.setObjectName("menubar")
        self.menuAccount = QtWidgets.QMenu(self.menubar)
        self.menuAccount.setObjectName("menuAccount")
        self.menuStatus = QtWidgets.QMenu(self.menubar)
        self.menuStatus.setObjectName("menuStatus")
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
        self.actionConnection = QtWidgets.QAction(PartisanMain)
        self.actionConnection.setObjectName("actionConnection")
        self.menuAccount.addAction(self.actionAddAccount)
        self.menuAccount.addAction(self.actionAccountInfo)
        self.menuAccount.addAction(self.actionLogout)
        self.menuStatus.addAction(self.actionConnection)
        self.menubar.addAction(self.menuAccount.menuAction())
        self.menubar.addAction(self.menuStatus.menuAction())

        self.retranslateUi(PartisanMain)
        QtCore.QMetaObject.connectSlotsByName(PartisanMain)

    def retranslateUi(self, PartisanMain):
        _translate = QtCore.QCoreApplication.translate
        PartisanMain.setWindowTitle(_translate("PartisanMain", "Partisan - Messenger"))
        self.labelContactList.setText(_translate("PartisanMain", "Contact List"))
        self.pushButtonRemove.setText(_translate("PartisanMain", "Remove"))
        self.pushButtonAdd.setText(_translate("PartisanMain", "Add"))
        self.lineInputMessage.setPlaceholderText(_translate("PartisanMain", "Type your message here..."))
        self.pushButtonSendMessage.setText(_translate("PartisanMain", "Send"))
        self.labelChat.setText(_translate("PartisanMain", "Chat"))
        self.pushButtonConfig.setText(_translate("PartisanMain", "..."))
        self.menuAccount.setTitle(_translate("PartisanMain", "Account"))
        self.menuStatus.setTitle(_translate("PartisanMain", "Status"))
        self.actionAddAccount.setText(_translate("PartisanMain", "Add Account..."))
        self.actionAccountInfo.setText(_translate("PartisanMain", "Account Info"))
        self.actionLogout.setText(_translate("PartisanMain", "Logout"))
        self.actionConnection.setText(_translate("PartisanMain", "Connection"))
