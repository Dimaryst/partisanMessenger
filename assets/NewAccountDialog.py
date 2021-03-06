# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'NewAccountDialog.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_DialogNewAccount(object):
    def setupUi(self, DialogNewAccount):
        DialogNewAccount.setObjectName("DialogNewAccount")
        DialogNewAccount.setWindowModality(QtCore.Qt.ApplicationModal)
        DialogNewAccount.resize(400, 240)
        DialogNewAccount.setMinimumSize(QtCore.QSize(380, 240))
        DialogNewAccount.setMaximumSize(QtCore.QSize(400, 240))
        self.verticalLayout = QtWidgets.QVBoxLayout(DialogNewAccount)
        self.verticalLayout.setObjectName("verticalLayout")
        self.lineEditUsername = QtWidgets.QLineEdit(DialogNewAccount)
        self.lineEditUsername.setText("")
        self.lineEditUsername.setObjectName("lineEditUsername")
        self.verticalLayout.addWidget(self.lineEditUsername)
        self.horizontalLayoutIp = QtWidgets.QHBoxLayout()
        self.horizontalLayoutIp.setObjectName("horizontalLayoutIp")
        self.labelIp = QtWidgets.QLabel(DialogNewAccount)
        self.labelIp.setObjectName("labelIp")
        self.horizontalLayoutIp.addWidget(self.labelIp)
        self.lineEditIp = QtWidgets.QLineEdit(DialogNewAccount)
        self.lineEditIp.setText("")
        self.lineEditIp.setPlaceholderText("")
        self.lineEditIp.setObjectName("lineEditIp")
        self.horizontalLayoutIp.addWidget(self.lineEditIp)
        self.verticalLayout.addLayout(self.horizontalLayoutIp)
        self.horizontalLayoutPort = QtWidgets.QHBoxLayout()
        self.horizontalLayoutPort.setObjectName("horizontalLayoutPort")
        self.labelPort = QtWidgets.QLabel(DialogNewAccount)
        self.labelPort.setObjectName("labelPort")
        self.horizontalLayoutPort.addWidget(self.labelPort)
        self.lineEditPort = QtWidgets.QLineEdit(DialogNewAccount)
        self.lineEditPort.setObjectName("lineEditPort")
        self.horizontalLayoutPort.addWidget(self.lineEditPort)
        self.verticalLayout.addLayout(self.horizontalLayoutPort)
        self.horizontalLayoutPassword = QtWidgets.QHBoxLayout()
        self.horizontalLayoutPassword.setObjectName("horizontalLayoutPassword")
        self.labelPassword = QtWidgets.QLabel(DialogNewAccount)
        self.labelPassword.setObjectName("labelPassword")
        self.horizontalLayoutPassword.addWidget(self.labelPassword)
        self.lineEditPassword = QtWidgets.QLineEdit(DialogNewAccount)
        self.lineEditPassword.setInputMask("")
        self.lineEditPassword.setText("")
        self.lineEditPassword.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEditPassword.setObjectName("lineEditPassword")
        self.horizontalLayoutPassword.addWidget(self.lineEditPassword)
        self.lineEditPasswordRepeat = QtWidgets.QLineEdit(DialogNewAccount)
        self.lineEditPasswordRepeat.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEditPasswordRepeat.setObjectName("lineEditPasswordRepeat")
        self.horizontalLayoutPassword.addWidget(self.lineEditPasswordRepeat)
        self.verticalLayout.addLayout(self.horizontalLayoutPassword)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.labelError = QtWidgets.QLabel(DialogNewAccount)
        self.labelError.setObjectName("labelError")
        self.horizontalLayout.addWidget(self.labelError)
        self.pushButtonCreate = QtWidgets.QPushButton(DialogNewAccount)
        self.pushButtonCreate.setDefault(True)
        self.pushButtonCreate.setObjectName("pushButtonCreate")
        self.horizontalLayout.addWidget(self.pushButtonCreate)
        self.pushButtonCancel = QtWidgets.QPushButton(DialogNewAccount)
        self.pushButtonCancel.setDefault(False)
        self.pushButtonCancel.setObjectName("pushButtonCancel")
        self.horizontalLayout.addWidget(self.pushButtonCancel)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(DialogNewAccount)
        QtCore.QMetaObject.connectSlotsByName(DialogNewAccount)

    def retranslateUi(self, DialogNewAccount):
        _translate = QtCore.QCoreApplication.translate
        DialogNewAccount.setWindowTitle(_translate("DialogNewAccount", "New Account"))
        self.lineEditUsername.setPlaceholderText(_translate("DialogNewAccount", "Account Name"))
        self.labelIp.setText(_translate("DialogNewAccount", "IP:"))
        self.labelPort.setText(_translate("DialogNewAccount", "Default Port:"))
        self.labelPassword.setText(_translate("DialogNewAccount", "Password:"))
        self.lineEditPassword.setPlaceholderText(_translate("DialogNewAccount", "Enter password"))
        self.lineEditPasswordRepeat.setPlaceholderText(_translate("DialogNewAccount", "Repeat password"))
        self.labelError.setText(_translate("DialogNewAccount", "Error (!)"))
        self.pushButtonCreate.setText(_translate("DialogNewAccount", "Create"))
        self.pushButtonCancel.setText(_translate("DialogNewAccount", "Cancel"))
