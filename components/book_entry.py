from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QWidget, QHBoxLayout, QLabel, QVBoxLayout, QFrame, QSizePolicy, QLineEdit, QInputDialog
from PyQt6.QtGui import QPixmap, QPainter, QBrush, QPen
from datastruct.book import Book
from typing import overload

class BookEntry(QFrame):
    """
    How a book is presented to the user
    """
    bookTitle: QLabel
    """ Label that displays the name of the book"""
    bookAuthor: QLabel
    """ Label that display the author of the book """
    bookPicture: QLabel
    """ Label that displays the image associated with the book"""
    bookPage: QLabel
    """ Label that displays the current page"""
    bookRating: QLabel
    """ Label that displays the rating of the book """

    @overload
    def __init__(self, book: Book) -> None : ...
    @overload
    def __init__(self, title:str, author: str, picturePath: str, page: int, rating: int) -> None : ...

    def __init__(
        self, a0 = "Unknown Book",
        a1 = "Unknown", a2: str = "resources/image/Book.png",
        a3: int = 0, a4: int = 0
        ):

        super().__init__()
        if (isinstance(a0, Book)):
            a0 : Book
            self._createUI(a0.title, a0.author, a2, a0.page, a0.rating)
        else:
            self._createUI(a0, a1, a2, a3, a4)
        self.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        
    
    def _createUI(self, title, author, picturePath, page, rating):
        # Title of the book
        self.bookTitle = QLabel(text=title)
        self.bookTitle.setProperty("cssClass", "BookTitle")

        # Initialise default picture of a book
        self.bookPicture = QLabel()
        picture = QPixmap(picturePath)
        picture = picture.scaled(200, 300, Qt.AspectRatioMode.KeepAspectRatioByExpanding)
        self.bookPicture.setPixmap(picture)

        # Other book info
        # Author
        self.bookAuthor = QWidget()
        layout = QHBoxLayout()
        bookAuthorLabel = QLabel("By ")
        bookAuthor = QLabel(author)
        self.bookAuthorInput = bookAuthor
        layout.addWidget(bookAuthorLabel)
        layout.addWidget(bookAuthor)
        layout.setContentsMargins(0,0,0,0)
        self.bookAuthor.setLayout(layout)

    
        # Page
        self.bookPage = QWidget()
        layout = QHBoxLayout()
        bookPageLabel = QLabel("Page: ")
        bookPage = QLabel(str(page))
        self.bookPageInput = bookPage
        layout.addWidget(bookPageLabel)
        layout.addWidget(bookPage)
        layout.setContentsMargins(0,0,0,0)
        self.bookPage.setLayout(layout)

        # Rating
        self.bookRating = QWidget()
        layout = QHBoxLayout()
        bookRatingLabel = QLabel("Rating: ")
        bookRating = QLabel(str(rating))
        self.bookRatingInput = bookRating
        layout.addWidget(bookRatingLabel)
        layout.addWidget(bookRating)
        layout.setContentsMargins(0,0,0,0)
        self.bookRating.setLayout(layout)

        layout = QHBoxLayout()
        layout.addWidget(self.bookPicture)

        content = QWidget()
        content.setStyleSheet("margin-left 2px;")
        bookInfoLayout = QVBoxLayout()
        content.setLayout(bookInfoLayout)

        bookInfoLayout.addWidget(self.bookTitle)
        bookInfoLayout.addWidget(self.bookAuthor)
        bookInfoLayout.addWidget(self.bookPage)
        bookInfoLayout.addWidget(self.bookRating)
        bookInfoLayout.addStretch(1)

        layout.addWidget(content)
        self.setLayout(layout)
    
    def toBook(self):
        return Book(
                self.bookTitle.text(), self.bookAuthorInput.text(),
                int(self.bookPageInput.text()), int(self.bookRatingInput.text())
                )
