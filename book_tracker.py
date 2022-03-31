import sys
from components.main_window import MainWindow
from PyQt6.QtWidgets import QApplication
from PyQt6.QtGui import QIcon
from helper.apply_styles import loadStyle
import ctypes

if __name__ == '__main__':

    myappid = u'book_tracker.0.2' # arbitrary string
    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)
    app = QApplication(sys.argv)
    window = MainWindow()
    loadStyle(window)
    window.showMaximized()
    sys.exit(app.exec())
