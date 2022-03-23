import sys
from widgets.main_window import MainWindow
from PyQt6.QtWidgets import QApplication

if __name__ == '__main__':

    app = QApplication(sys.argv)
    window = MainWindow()
    window.loadStyle("styles/main-window.css")
    window.show()
    sys.exit(app.exec())