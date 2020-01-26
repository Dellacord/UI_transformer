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

    py_path = QtWidgets.QFileDialog.getOpenFileName()[0]#Выбор файла

    serch_py = re.search(r'test.py', str (py_path))# В случае отсутствия искомого, возвращает  None

    if serch_py != None:
        ui.label_4.setPixmap(QtGui.QPixmap("check.png"))
        return serch_py
    else:
        ui.label_4.setPixmap(QtGui.QPixmap("cross.png"))

def ui_file():
    ''' Вызов проводника для определения пути к *.ui'''

    ui_path = QtWidgets.QFileDialog.getOpenFileName()[0]

    serch_ui = re.search(r'.ui', str (ui_path))# В случае отсутствия искомого, возвращает  None

    if serch_ui != None:
        ui.label_5.setPixmap(QtGui.QPixmap("check.png"))
        return serch_ui
    else:
        ui.label_5.setPixmap(QtGui.QPixmap("cross.png"))

def py_dir():
    ''' Выбор папки для .py файла'''

    dialog = QFileDialog()
    foo_dir = dialog.getExistingDirectory()#Выбор папки

    if len(foo_dir) > 0:
        ui.label_6.setPixmap(QtGui.QPixmap("check.png"))
        return foo_dir
    else:
        ui.label_6.setPixmap(QtGui.QPixmap("cross.png"))


#def tran(pf,uf,dr):
    #print(pf,uf,dr)

a = ''
b = ''
c = ''

a = ui.pushButton.clicked.connect(py_file)
b = ui.pushButton_2.clicked.connect(ui_file)
c = ui.pushButton_3.clicked.connect(py_dir)
#ui.pushButton_4.clicked.connect(tran)


#Запуск программы
sys.exit(app.exec_())