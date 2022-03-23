from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QWidget, QHBoxLayout, QLabel, QVBoxLayout, QFrame, QSizePolicy, QLineEdit, QInputDialog
from PyQt6.QtGui import QPixmap, QPainter, QBrush, QPen

class BookEntry(QFrame):
    """
    How a book is presented to the user
    """

    bookTitle: QLabel
    """Holds the name of the book"""
    bookPicture: QLabel
    """Holds the image associated with the book"""

    def __init__(self, parent: QWidget=None, title:str = "Empty Book"):
        super().__init__(parent)
        # Title of the book
        self.bookTitle = QLabel(text=title)
        self.bookTitle.setProperty("cssClass", "BookTitle")

        # Initialise default picture of a book
        self.bookPicture = QLabel()
        picture = QPixmap("resources/image/Book.png")
        picture = picture.scaled(200, 300, Qt.AspectRatioMode.KeepAspectRatioByExpanding)
        self.bookPicture.setPixmap(picture)

        layout = QHBoxLayout()
        layout.addWidget(self.bookPicture)

        bookInfoLayout = QVBoxLayout()
        bookInfoLayout.addWidget(self.bookTitle)
        bookInfoLayout.addWidget(QInputDialog())
        bookInfoLayout.addWidget(QLabel("Ratings: 0/5"))
        layout.addLayout(bookInfoLayout)
        self.setLayout(layout)



        # layout = QVBoxLayout()
        # bookInfoLayout = QVBoxLayout()
        # bookInfoLayout.setAlignment(Qt.AlignmentFlag.AlignTop)
        # b = QLabel(text="Page:")
        # a = QLineEdit("0", b)
        # a.setEnabled(False)

        # bookInfoLayout.addWidget(QInputDialog())
        # bookInfoLayout.addWidget(QLabel(text="Ratings: 0/5"))

        # bookContentLayout = QHBoxLayout()
        # bookContentLayout.setAlignment(Qt.AlignmentFlag.AlignLeft)
        # bookContentLayout.addWidget(self.bookPicture)
        # bookContentLayout.addLayout(bookInfoLayout)
        # layout.addWidget(self.bookTitle)
        # layout.addLayout(bookContentLayout)
        # self.setLayout(layout)
