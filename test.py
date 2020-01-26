from PyQt5.QtWidgets import QFileDialog, QDialog
#from definitions import ROOT_DIR
from PyQt5 import QtCore


def FileDialog(directory='', forOpen=True, fmt='', isFolder=False):
    options = QFileDialog.Options()
    options |= QFileDialog.DontUseNativeDialog
    options |= QFileDialog.DontUseCustomDirectoryIcons
    dialog = QFileDialog()
    dialog.setOptions(options)

    dialog.setFilter(dialog.filter() | QtCore.QDir.Hidden)

    # ARE WE TALKING ABOUT FILES OR FOLDERS
    if isFolder:
        dialog.setFileMode(QFileDialog.DirectoryOnly)
    else:
        dialog.setFileMode(QFileDialog.AnyFile)
    # OPENING OR SAVING
    dialog.setAcceptMode(QFileDialog.AcceptOpen) if forOpen else dialog.setAcceptMode(QFileDialog.AcceptSave)

    # SET FORMAT, IF SPECIFIED
    #if fmt != '' and isFolder is False:
        #dialog.setDefaultSuffix(fmt)
        #dialog.setNameFilters([f'{fmt} (*.{fmt})'])

    # SET THE STARTING DIRECTORY
    if directory != '':
        dialog.setDirectory(str(directory))
    else:
        dialog.setDirectory(str(ROOT_DIR))


    if dialog.exec_() == QDialog.Accepted:
        path = dialog.selectedFiles()[0]  # returns a list
        return path
    else:
        return ''