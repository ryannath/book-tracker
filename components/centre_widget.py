from typing import Optional
from PyQt6.QtWidgets import QWidget, QPushButton, QVBoxLayout, QSizePolicy, QGridLayout, QHBoxLayout

from components.book_entry import BookEntry

class CentreWidget(QWidget):

    def __init__(self, parent: Optional[QWidget]=None) -> None:
        super().__init__(parent)
        self._createUI()

    def addBook(self, bookEntry: BookEntry):
        if self.j < 2:
            self.contentLayout.addWidget(bookEntry, self.j, self.i)
            self.i += 1
            if self.i > 2:
                self.j += 1
                self.i = 0

    def _createUI(self) -> None:
        # The controls above the grid of books
        # example application: add new books to the grid
        self.controlsLayout = QHBoxLayout()

        self.newBookButton = QPushButton("Add New Book")
        # self.newBookButton.clicked.connect(self.launchNewBookWindow)
        self.removeBookButton = QPushButton("Remove Book")
        self.prevPageButton = QPushButton("<")
        self.nextPageButton = QPushButton(">")

        self.controlsLayout.addWidget(self.newBookButton)
        self.controlsLayout.addWidget(self.removeBookButton)
        self.controlsLayout.addWidget(self.prevPageButton)
        self.controlsLayout.addWidget(self.nextPageButton)
        # Leave space from the end of the controls to the side of the widget
        self.controlsLayout.addStretch(1)


        # The grid of books, main content
        self.contentLayout = QGridLayout()
        self.i = 0
        self.j = 0

        # Adds a stretch of i to column index 2
        self.contentLayout.setColumnStretch(3, 1)

        # Main layout
        layout = QVBoxLayout()
        layout.addLayout(self.controlsLayout)
        layout.addLayout(self.contentLayout)
        # Add a space between grid and the bottom of the widget
        layout.addStretch(1)

        self.setLayout(layout)
