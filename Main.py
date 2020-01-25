#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from PyQt5 import QtCore, QtGui, QtWidgets
import mywin

#def py_file():
    #py_path = QtWidgets.QFileDialog.getOpenFileName()
    #print (py_path)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = mywin.Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    #ui.pushButton.clicked(py_file())
    sys.exit(app.exec_())