# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ContactInfoDialog.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_DialogContactInfo(object):
    def setupUi(self, DialogContactInfo):
        DialogContactInfo.setObjectName("DialogContactInfo")
        DialogContactInfo.setWindowModality(QtCore.Qt.ApplicationModal)
        DialogContactInfo.resize(480, 240)
        DialogContactInfo.setMinimumSize(QtCore.QSize(480, 240))
        DialogContactInfo.setMaximumSize(QtCore.QSize(480, 240))
        self.verticalLayout = QtWidgets.QVBoxLayout(DialogContactInfo)
        self.verticalLayout.setObjectName("verticalLayout")
        self.lineEditUsername = QtWidgets.QLineEdit(DialogContactInfo)
        self.lineEditUsername.setObjectName("lineEditUsername")
        self.verticalLayout.addWidget(self.lineEditUsername)
        self.lineEditUuid = QtWidgets.QLineEdit(DialogContactInfo)
        self.lineEditUuid.setObjectName("lineEditUuid")
        self.verticalLayout.addWidget(self.lineEditUuid)
        self.horizontalLayoutIp = QtWidgets.QHBoxLayout()
        self.horizontalLayoutIp.setObjectName("horizontalLayoutIp")
        self.labelIp = QtWidgets.QLabel(DialogContactInfo)
        self.labelIp.setObjectName("labelIp")
        self.horizontalLayoutIp.addWidget(self.labelIp)
        self.lineEditIp = QtWidgets.QLineEdit(DialogContactInfo)
        self.lineEditIp.setObjectName("lineEditIp")
        self.horizontalLayoutIp.addWidget(self.lineEditIp)
        self.verticalLayout.addLayout(self.horizontalLayoutIp)
        self.horizontalLayoutPort = QtWidgets.QHBoxLayout()
        self.horizontalLayoutPort.setObjectName("horizontalLayoutPort")
        self.labelPort = QtWidgets.QLabel(DialogContactInfo)
        self.labelPort.setObjectName("labelPort")
        self.horizontalLayoutPort.addWidget(self.labelPort)
        self.lineEditPort = QtWidgets.QLineEdit(DialogContactInfo)
        self.lineEditPort.setObjectName("lineEditPort")
        self.horizontalLayoutPort.addWidget(self.lineEditPort)
        self.verticalLayout.addLayout(self.horizontalLayoutPort)
        self.horizontalLayoutInterval = QtWidgets.QHBoxLayout()
        self.horizontalLayoutInterval.setObjectName("horizontalLayoutInterval")
        self.labelInterval = QtWidgets.QLabel(DialogContactInfo)
        self.labelInterval.setObjectName("labelInterval")
        self.horizontalLayoutInterval.addWidget(self.labelInterval)
        self.lineEditInterval = QtWidgets.QLineEdit(DialogContactInfo)
        self.lineEditInterval.setObjectName("lineEditInterval")
        self.horizontalLayoutInterval.addWidget(self.lineEditInterval)
        self.verticalLayout.addLayout(self.horizontalLayoutInterval)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.labelError = QtWidgets.QLabel(DialogContactInfo)
        self.labelError.setObjectName("labelError")
        self.horizontalLayout.addWidget(self.labelError)
        self.pushButtonSave = QtWidgets.QPushButton(DialogContactInfo)
        self.pushButtonSave.setObjectName("pushButtonSave")
        self.horizontalLayout.addWidget(self.pushButtonSave)
        self.pushButtonCancel = QtWidgets.QPushButton(DialogContactInfo)
        self.pushButtonCancel.setDefault(True)
        self.pushButtonCancel.setObjectName("pushButtonCancel")
        self.horizontalLayout.addWidget(self.pushButtonCancel)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(DialogContactInfo)
        QtCore.QMetaObject.connectSlotsByName(DialogContactInfo)

    def retranslateUi(self, DialogContactInfo):
        _translate = QtCore.QCoreApplication.translate
        DialogContactInfo.setWindowTitle(_translate("DialogContactInfo", "Contact"))
        self.lineEditUsername.setPlaceholderText(_translate("DialogContactInfo", "Nickname"))
        self.lineEditUuid.setPlaceholderText(_translate("DialogContactInfo", "UUID"))
        self.labelIp.setText(_translate("DialogContactInfo", "IP:"))
        self.labelPort.setText(_translate("DialogContactInfo", "Default Port:"))
        self.labelInterval.setText(_translate("DialogContactInfo", "Connection interval (seconds):"))
        self.labelError.setText(_translate("DialogContactInfo", "Error (!)"))
        self.pushButtonSave.setText(_translate("DialogContactInfo", "Save"))
        self.pushButtonCancel.setText(_translate("DialogContactInfo", "Cancel"))
