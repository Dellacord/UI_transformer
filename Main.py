#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import (QMainWindow, QTextEdit, QAction, QFileDialog, QApplication)
from mywin import Ui_MainWindow
import re
import os
import shutil

#Создаем аппликацию
app = QtWidgets.QApplication(sys.argv)

#Создаем форму и инициализируем UI
MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)
MainWindow.show()

''' Текст программы '''
def comp_win():
    app1 = QtWidgets.QApplication(sys.argv)
    CompWindow = QtWidgets.QMainWindow()
    cp_ui = cp_win.Ui_MainWindow()
    cp_ui.setupUi(CompWindow)
    CompWindow.show()
    sys.exit(app1.exec_())


class transform():

    ui_fl = ''
    foo_dir = ''
    py_path = ''
    check = [0,0,0]

    dir = sys.exec_prefix #Рабочая папка Phython
    fil = []

    for i in os.walk(dir): # Рекурсивный просмотр папки
        fil.append(i)

    for address, dirs, files in fil: # Перебор всех файлов и папок
        for file in files:
            if file == 'pyuic5.bat':
                ui.label_4.setPixmap(QtGui.QPixmap("check.png"))
                py_path = str(address + '\\' + file)
                ui.label.setText("PYQT5 module downloaded")
                check[0] = 1

    def ui_file(self):
        ''' Вызов проводника для определения пути к *.ui'''

        transform.ui_fl = QtWidgets.QFileDialog.getOpenFileName()[0]
        serch_ui = re.search(r'.ui', str(transform.ui_fl))  # В случае отсутствия искомого, возвращает  None

        if serch_ui != None:
            ui.label_5.setPixmap(QtGui.QPixmap("check.png"))
            transform.check[1] = 1
        else:
            ui.label_5.setPixmap(QtGui.QPixmap("cross.png"))

    def py_dir(self):
        ''' Выбор папки для .py файла'''

        transform.foo_dir = QFileDialog.getExistingDirectory()  # Выбор папки

        if len(transform.foo_dir) > 0:
            ui.label_6.setPixmap(QtGui.QPixmap("check.png"))
            transform.check[2] = 1
        else:
            ui.label_6.setPixmap(QtGui.QPixmap("cross.png"))

    def tran(self):#создает фаил py в дериктории программы
        '''  os.system('command') - выполнение команды в консоли CMD
         move c:\test\file1.txt D:\folder2\file2.txt -
         перенести файл file1.txt из каталога test диска C: в каталог folder2 диска D: под именем file2.txt
         os.getcwd() получение текущей рабочей дериктории'''
        if transform.check[0] + transform.check[1] + transform.check[2] == 3 and len(ui.textEdit.text()) != 0:
            app_trans = transform.py_path + ' ' + str(transform.ui_fl) + ' -o ' + ui.textEdit.text() + '.py'
            os.system(app_trans)
            app_move_from = os.getcwd() + '\\' + ui.textEdit.text() + '.py'
            app_move_to = transform.foo_dir
            shutil.move(app_move_from, app_move_to) # перемещение файла
            ui.label_7.setPixmap(QtGui.QPixmap("check.png"))



sh = transform
ui.pushButton_2.clicked.connect(sh.ui_file)
ui.pushButton_3.clicked.connect(sh.py_dir)
ui.pushButton_4.clicked.connect(sh.tran)

#Запуск программы
sys.exit(app.exec_())
