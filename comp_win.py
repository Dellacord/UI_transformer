# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:/Development/UI_transformer_Test/test.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 300)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(50, 100, 111, 41))
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(60, 180, 201, 41))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Compilation"))
        self.pushButton.setText(_translate("Form", "Start"))

