from PyQt6.QtCore import Qt
from PyQt6.QtGui import QAction
from PyQt6.QtWidgets import (
    QApplication, QMenu, QMainWindow, QWidget,
    QHBoxLayout, QPushButton, QLineEdit,
    QVBoxLayout)

from functions.actions import openProfile, saveProfile

from typing import Dict
from datastruct.book import Book

class MainWindow(QMainWindow):
    centralWidget: QWidget
    """Central widget of the main window"""
    openAction: QAction
    saveAction: QAction
    data: Dict[str, Book] = {}

    def __init__(self, parent: QWidget = None) -> None:
        """Initialise main window"""
        super().__init__(parent)
        self.setWindowTitle("Book Tracker")
        self.resize(500, 500)
        self.centralWidget = QWidget()
        self.setCentralWidget(self.centralWidget)
        self._createActions()
        self._createMenuBar()


    def loadStyle(self, path: str) -> None:
        with open(path, 'r') as f:
            self.setStyleSheet(f.read())
        
    
    def _createActions(self) -> None:
        self.openAction = QAction("&Open File...", self)
        self.openAction.setShortcut("Ctrl+O")
        self.openAction.setStatusTip("Open a user profile history")
        self.openAction.triggered.connect(openProfile)

        self.saveAction = QAction("&Save As", self)
        self.saveAction.setShortcut("Ctrl+S")
        self.saveAction.setStatusTip("Save the current user profile history")
        self.saveAction.triggered.connect(lambda : saveProfile(self.data))
        
    def _createMenuBar(self) -> None:
        menuBar = self.menuBar()
        fileMenu = QMenu("File", self)
        fileMenu.addAction(self.openAction)
        fileMenu.addAction(self.saveAction)
        menuBar.addMenu(fileMenu)


    def createUI(self) -> None:
        
        self.path = QLineEdit()
        self.label1.setPlaceholderText("Select save file")
        button1 = QPushButton("Browse")
        self.label2 = QLineEdit("Yeet")
        button2 = QPushButton("Browse")
        button1.clicked.connect(self.browseFile)
        layout1 = QHBoxLayout()
        layout2 = QHBoxLayout()

        layout1.addWidget(self.label1)
        layout1.addWidget(button1)

        layout2.addWidget(self.label2)
        layout2.addWidget(button2)
        bigLayout = QVBoxLayout()
        bigLayout.addLayout(layout1)
        bigLayout.addLayout(layout2)
        bigLayout.setAlignment(Qt.AlignmentFlag.AlignTop)

        self.widget = QWidget()
        self.widget.setLayout(bigLayout)
        self.setCentralWidget(self.widget)
    

if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    window = MainWindow()
    # window.loadStyle("styles/main-window.css")
    window.show()
    sys.exit(app.exec())