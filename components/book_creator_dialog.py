from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import (
    QDialog, QLabel, QHBoxLayout, QFormLayout, QLineEdit,
    QDialogButtonBox
)

class BookCreatorDialog(QDialog):
    def __init__(self):
        super().__init__()
        self._createUI()
    
    def _createUI(self):
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
        self.bookAuthor = QLineEdit()
        self.bookPage = QLineEdit()
        self.bookRating = QLineEdit()

        bookInfoLayout.addRow("Title", self.bookTitle)
        bookInfoLayout.addRow("Author", self.bookAuthor)
        bookInfoLayout.addRow("Page", self.bookPage)
        bookInfoLayout.addRow("Rating", self.bookRating)
        self.button = QDialogButtonBox(QDialogButtonBox.StandardButton.Ok | QDialogButtonBox.StandardButton.Cancel)
        self.button.accepted.connect(self.accept)
        self.button.rejected.connect(self.reject)
        bookInfoLayout.addWidget(self.button)
        layout.addLayout(bookInfoLayout)
        self.setLayout(layout)
