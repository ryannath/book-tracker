from typing import Optional
from widgets.book_entry import BookEntry
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QDialog, QWidget, QHBoxLayout, QVBoxLayout, QLabel, QLineEdit, QFormLayout, QDialogButtonBox
from PyQt6.QtGui import QPixmap

class BookEntryCreator(QDialog):
    def __init__(self, parent: Optional[QWidget] = None):
        super().__init__(parent)

        # Title of the book
        self.bookTitle = QLabel(text="Book Title")
        self.bookTitle.setProperty("cssClass", "BookTitle")

        # Initialise default picture of a book
        self.bookPicture = QLabel()
        picture = QPixmap("resources/image/Book.png")
        picture = picture.scaled(200, 300, Qt.AspectRatioMode.KeepAspectRatioByExpanding)
        self.bookPicture.setPixmap(picture)

        layout = QHBoxLayout()
        layout.addWidget(self.bookPicture)

        bookInfoLayout = QFormLayout()
        self.bookTitle = QLineEdit()
        self.bookPage = QLineEdit()
        self.bookRating = QLineEdit()

        bookInfoLayout.addRow("Title", self.bookTitle)
        bookInfoLayout.addRow("Page", self.bookPage)
        bookInfoLayout.addRow("Rating", self.bookRating)
        self.button = QDialogButtonBox(QDialogButtonBox.StandardButton.Ok | QDialogButtonBox.StandardButton.Cancel)
        self.button.accepted.connect(self.accept)
        self.button.rejected.connect(self.reject)
        bookInfoLayout.addWidget(self.button)
        layout.addLayout(bookInfoLayout)
        self.setLayout(layout)

    def _createUI(self):
        pass