import pickle
from PyQt6.QtGui import QAction, QIcon
from PyQt6.QtWidgets import QMenu, QMainWindow, QWidget, QFileDialog
from components.centre_widget import CentreWidget
from typing import Dict, Optional
from components.book_creator import BookCreator


from datastruct.book import Book

class MainWindow(QMainWindow):
    """Main UI of the program which users will interact with"""

    # Attributes **************************************************************
    centralWidget: QWidget
    """Central widget of the main window"""
    openAction: QAction
    """Action to open a saved profile through 'file' menu in menubar"""
    saveAction: QAction
    """Action to save the current profile through 'file' menu in menubar"""
    data: Dict[str, Book] = {}  # TODO: perhaps refactor, divide up the logic
    """Holds the data of the current loaded profile"""

    # *************************************************************************


    # Methods *****************************************************************
    def __init__(self, parent: QWidget = None) -> None:
        """Initialise main window"""

        super().__init__(parent)
        self.setWindowTitle("Book Tracker")
        self.resize(500, 500)

        self.centralWidget = CentreWidget()
        self.setCentralWidget(self.centralWidget)
        self.creator = BookCreator()
        self.centralWidget.newBookButton.clicked.connect(self.creator.launch_creator)
        self.creator.created.connect(self.addBook)

        self._loadRecent()
        # Initialise actions and the menu bar
        self._createActions()
        self._createMenuBar()
        self.setWindowIcon(QIcon("resources/image/book tracker logo.svg"))




    def addBook(self):
        newBook = self.creator.newBook.toBook()
        self.data[newBook.title] = newBook
        self.centralWidget.addBook(self.creator.newBook)
        print(self.data)


    def loadStyle(self, path: str) -> None:
        """Applies all styling from given file"""
        with open(path, 'r') as f:
            self.stylePath = f.read()
            self.setStyleSheet(self.stylePath)
        
    def _loadRecent(self):
        try:
            with open("saves/.recent", "rb") as f:
                profilePath = f.read()
                with open(profilePath, "rb") as f:
                    self.data = pickle.load(f)
                    print(self.data)
                for entry in self.data.values():
                    self.creator.createBook(entry)
                    self.centralWidget.addBook(self.creator.newBook)

        except Exception as e:
            print(e)

    def _createActions(self) -> None:
        self.openAction = QAction("&Open File...", self)
        self.openAction.setShortcut("Ctrl+O")
        self.openAction.setStatusTip("Open a user profile history")
        self.openAction.triggered.connect(self.openProfile)

        self.saveAction = QAction("&Save As", self)
        self.saveAction.setShortcut("Ctrl+S")
        self.saveAction.setStatusTip("Save the current user profile history")

        # Need to send 'data' stored in this object
        # to be saved using saveProfile
        self.saveAction.triggered.connect(self.saveProfile)


    def _createMenuBar(self) -> None:
        # QMainWindow already defines a menuBar, simply access it using
        # the method
        menuBar = self.menuBar()

        # one menuBar contains several menus, here initialise a 'File' menu
        fileMenu = QMenu("File", self)
        fileMenu.addAction(self.openAction)
        fileMenu.addAction(self.saveAction)
        menuBar.addMenu(fileMenu)


    def openProfile(self) -> None:
        name = QFileDialog.getOpenFileName(caption="Open File", filter="Profile Files (*.bt)")[0]
        if name:
            with open(name, "rb") as f:
                self.data = pickle.load(f)
                print(self.data)
            with open("saves/.recent", "w") as f:
                f.write(name)

    def saveProfile(self) -> None:
        name = QFileDialog.getSaveFileName(caption="Save As", filter="Profile Files (*.bt)")[0]
        if name:
            with open(name, "wb") as f:
                pickle.dump(self.data, f)
            with open("saves/.recent", "w") as f:
                f.write(name)
        
    