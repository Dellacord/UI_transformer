#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import (QMainWindow, QTextEdit, QAction, QFileDialog, QApplication)
from mywin import Ui_MainWindow
import re

#Создаем аппликацию
app = QtWidgets.QApplication(sys.argv)

#Создаем форму и инициализируем UI
MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)
MainWindow.show()

''' Текст программы '''

def py_file():
    ''' Вызов проводника для определения пути к Python.exe
sys.executable - полный путь до Python.exe'''

    py_path = QtWidgets.QFileDialog.getOpenFileName()[0]

    serch_py = re.search(r'test.py', str (py_path))# В случае отсутствия искомого, возвращает  None

    if serch_py != None:
        ui.label_4.setPixmap(QtGui.QPixmap("check.png"))
    else:
        ui.label_4.setPixmap(QtGui.QPixmap("cross.png"))

def ui_file():
    ''' Вызов проводника для определения пути к *.ui'''

    ui_path = QtWidgets.QFileDialog.getOpenFileName()[0]

    serch_ui = re.search(r'.ui', str (ui_path))# В случае отсутствия искомого, возвращает  None

    if serch_ui != None:
        ui.label_5.setPixmap(QtGui.QPixmap("check.png"))
    else:
        ui.label_5.setPixmap(QtGui.QPixmap("cross.png"))

ui.pushButton.clicked.connect(py_file)
ui.pushButton_2.clicked.connect(ui_file)

#Запуск программы
sys.exit(app.exec_())