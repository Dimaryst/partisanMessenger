# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'newContact.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_DialogNewContact(object):
    def setupUi(self, DialogNewContact):
        DialogNewContact.setObjectName("DialogNewContact")
        DialogNewContact.setWindowModality(QtCore.Qt.ApplicationModal)
        DialogNewContact.resize(420, 160)
        DialogNewContact.setMinimumSize(QtCore.QSize(400, 160))
        DialogNewContact.setMaximumSize(QtCore.QSize(420, 180))
        self.verticalLayout = QtWidgets.QVBoxLayout(DialogNewContact)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayoutIp = QtWidgets.QHBoxLayout()
        self.horizontalLayoutIp.setObjectName("horizontalLayoutIp")
        self.labelIp = QtWidgets.QLabel(DialogNewContact)
        self.labelIp.setObjectName("labelIp")
        self.horizontalLayoutIp.addWidget(self.labelIp)
        self.lineEditIp = QtWidgets.QLineEdit(DialogNewContact)
        self.lineEditIp.setText("")
        self.lineEditIp.setPlaceholderText("")
        self.lineEditIp.setObjectName("lineEditIp")
        self.horizontalLayoutIp.addWidget(self.lineEditIp)
        self.verticalLayout.addLayout(self.horizontalLayoutIp)
        self.horizontalLayoutName = QtWidgets.QHBoxLayout()
        self.horizontalLayoutName.setObjectName("horizontalLayoutName")
        self.labelName = QtWidgets.QLabel(DialogNewContact)
        self.labelName.setObjectName("labelName")
        self.horizontalLayoutName.addWidget(self.labelName)
        self.lineEditName = QtWidgets.QLineEdit(DialogNewContact)
        self.lineEditName.setObjectName("lineEditName")
        self.horizontalLayoutName.addWidget(self.lineEditName)
        self.verticalLayout.addLayout(self.horizontalLayoutName)
        self.horizontalLayoutButtons = QtWidgets.QHBoxLayout()
        self.horizontalLayoutButtons.setObjectName("horizontalLayoutButtons")
        self.labelError = QtWidgets.QLabel(DialogNewContact)
        self.labelError.setObjectName("labelError")
        self.horizontalLayoutButtons.addWidget(self.labelError)
        self.pushButtonAdd = QtWidgets.QPushButton(DialogNewContact)
        self.pushButtonAdd.setDefault(True)
        self.pushButtonAdd.setObjectName("pushButtonAdd")
        self.horizontalLayoutButtons.addWidget(self.pushButtonAdd)
        self.pushButtonCancel = QtWidgets.QPushButton(DialogNewContact)
        self.pushButtonCancel.setDefault(False)
        self.pushButtonCancel.setObjectName("pushButtonCancel")
        self.horizontalLayoutButtons.addWidget(self.pushButtonCancel)
        self.verticalLayout.addLayout(self.horizontalLayoutButtons)

        self.retranslateUi(DialogNewContact)
        QtCore.QMetaObject.connectSlotsByName(DialogNewContact)

    def retranslateUi(self, DialogNewContact):
        _translate = QtCore.QCoreApplication.translate
        DialogNewContact.setWindowTitle(_translate("DialogNewContact", "New Contact"))
        self.labelIp.setText(_translate("DialogNewContact", "IP Address:"))
        self.labelName.setText(_translate("DialogNewContact", "Contact name:"))
        self.labelError.setText(_translate("DialogNewContact", "Error (!)"))
        self.pushButtonAdd.setText(_translate("DialogNewContact", "Add"))
        self.pushButtonCancel.setText(_translate("DialogNewContact", "Cancel"))
