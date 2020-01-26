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

class transform():

    ui_path = ''
    foo_dir = ''
    py_path = sys.executable  # команда для вывода пути к python.exe

    serch_py = re.search(r'python.exe', str(py_path))  # В случае отсутствия искомого, возвращает  None

    if serch_py != None:
        ui.label_4.setPixmap(QtGui.QPixmap("check.png"))
    else:
        ui.label_4.setPixmap(QtGui.QPixmap("cross.png"))
        ui.label.setText("Python.exe file not found:")




    def ui_file(self):
        ''' Вызов проводника для определения пути к *.ui'''

        transform.ui_path = QtWidgets.QFileDialog.getOpenFileName()[0]

        serch_ui = re.search(r'.ui', str(transform.ui_path))  # В случае отсутствия искомого, возвращает  None

        if serch_ui != None:
            ui.label_5.setPixmap(QtGui.QPixmap("check.png"))
        else:
            ui.label_5.setPixmap(QtGui.QPixmap("cross.png"))

    def py_dir(self):
        ''' Выбор папки для .py файла'''

        transform.foo_dir = QFileDialog.getExistingDirectory()  # Выбор папки

        if len(transform.foo_dir) > 0:
            ui.label_6.setPixmap(QtGui.QPixmap("check.png"))
        else:
            ui.label_6.setPixmap(QtGui.QPixmap("cross.png"))

    def tran():
        print(transform.py_path, transform.ui_path, transform.foo_dir)

sh = transform
ui.pushButton_2.clicked.connect(sh.ui_file)
ui.pushButton_3.clicked.connect(sh.py_dir)
ui.pushButton_4.clicked.connect(sh.tran)

#Запуск программы
sys.exit(app.exec_())