from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QWidget, QHBoxLayout, QLabel, QVBoxLayout, QFrame, QSizePolicy, QLineEdit, QInputDialog
from PyQt6.QtGui import QPixmap, QPainter, QBrush, QPen

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


    def __init__(
        self, parent: QWidget=None, title: str = "Unknown Book",
        author: str = "Unknown", picturePath: str = "resources/image/Book.png",
        page: int = 0, rating: int = 0
        ):
        super().__init__(parent)
        self._createUI(title, author, picturePath, page, rating)
        
    
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
        layout.addWidget(bookAuthorLabel)
        layout.addWidget(bookAuthor)
        layout.setContentsMargins(0,0,0,0)
        self.bookAuthor.setLayout(layout)

    
        # Page
        self.bookPage = QWidget()
        layout = QHBoxLayout()
        bookPageLabel = QLabel("Page: ")
        bookPage = QLabel(str(page))
        layout.addWidget(bookPageLabel)
        layout.addWidget(bookPage)
        layout.setContentsMargins(0,0,0,0)
        self.bookPage.setLayout(layout)

        # Rating
        self.bookRating = QWidget()
        layout = QHBoxLayout()
        bookRatingLabel = QLabel("Rating: ")
        bookRating = QLabel(str(rating))
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
