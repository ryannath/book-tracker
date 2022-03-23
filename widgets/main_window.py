from PyQt6.QtGui import QAction
from PyQt6.QtWidgets import QMenu, QMainWindow, QWidget

from functions.actions import openProfile, saveProfile
from widgets.centre_widget import CentreWidget
from typing import Dict
from datastruct.book import Book

class MainWindow(QMainWindow):
    """Main UI of the program which users will interact with"""

    # Attributes **************************************************************
    centralWidget: QWidget
    """Central widget of the main window"""
    openAction: QAction
    """Action to open a saved profile through file menu in menubar"""
    saveAction: QAction
    """Action to save the current profile through 'file' menu in menubar"""
    data: Dict[str, Book] = {}  # TODO: perhaps refactor, divide up the logic
    """Holds the data of the current loaded profile"""

    # *************************************************************************


    # *************************************************************************
    def __init__(self, parent: QWidget = None) -> None:
        """Initialise main window"""

        super().__init__(parent)
        self.setWindowTitle("Book Tracker")
        self.resize(500, 500)

        # TODO: refactor centralWidget  
        self.centralWidget = CentreWidget()
        self.setCentralWidget(self.centralWidget)

        # Initialise actions and the menu bar
        self._createActions()
        self._createMenuBar()


    def loadStyle(self, path: str) -> None:
        """Applies all styling from given file"""
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
        # Need to send 'data' stored in this object
        # to be saved using saveProfile
        self.saveAction.triggered.connect(lambda : saveProfile(self.data))


    def _createMenuBar(self) -> None:
        # QMainWindow already defines a menuBar, simply access it using
        # the method
        menuBar = self.menuBar()

        # one menuBar contains several menus, here initialise a 'File' menu
        fileMenu = QMenu("File", self)
        fileMenu.addAction(self.openAction)
        fileMenu.addAction(self.saveAction)
        menuBar.addMenu(fileMenu)
