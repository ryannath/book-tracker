from typing import Optional
from PyQt6.QtWidgets import QWidget, QPushButton, QVBoxLayout, QSizePolicy, QGridLayout, QHBoxLayout
from PyQt6.QtCore import Qt
from widgets.book_entry import BookEntry
from widgets.book_entry_creator import BookEntryCreator

class CentreWidget(QWidget):

    controlsLayout: QHBoxLayout
    """ Contains buttons to control the grid of books """
    contentLayout: QGridLayout
    """ Contains a grid of book """
    newBookButton: QPushButton
    """ Button to add a new button to the profile """
    bookCreator: BookEntryCreator
    """ Modal window that pops up for user to input in book information"""

    def __init__(self, parent: Optional[QWidget]=None) -> None:
        super().__init__(parent)
        self._createUI()

    def _createUI(self) -> None:
        # The controls above the grid of books
        # example application: add new books to the grid
        self.controlsLayout = QHBoxLayout()
        self.newBookButton = QPushButton("Add New Book")
        self.newBookButton.clicked.connect(self.launchNewBookWindow)
        self.controlsLayout.addWidget(self.newBookButton)
        # Leave space from the end of the controls to the side of the widget
        self.controlsLayout.addStretch(1)


        # The grid of books, main content
        self.contentLayout = QGridLayout()
        self.contentLayout.addWidget(BookEntry(), 1, 0)
        self.contentLayout.addWidget(BookEntry(), 1, 1)
        # Adds a stretch of i to column index 2
        self.contentLayout.setColumnStretch(4, 1)

        # Main layout
        layout = QVBoxLayout()
        layout.addLayout(self.controlsLayout)
        layout.addLayout(self.contentLayout)
        # Add a space between grid and the bottom of the widget
        layout.addStretch(1)

        self.setLayout(layout)


    def launchNewBookWindow(self):
        bookCreator = BookEntryCreator()
        bookCreator.setStyleSheet(self.parent().stylePath)
        success = bookCreator.exec()
        if (BookEntryCreator.DialogCode.Accepted == success):
            self.contentLayout.addWidget(BookEntry(None, bookCreator.bookTitle.text()))

