# from PyQt6.QtWidgets impor
from PyQt6.QtCore import pyqtSignal
from PyQt6.QtWidgets import QWidget

from components.book_creator_dialog import BookCreatorDialog
from components.book_entry import BookEntry

class BookCreator(QWidget):
    created = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.bookTitle = "Unknown Book"
        self.bookAuthor = "Unknown"
        self.picturePath = "resources/image/Book.png"
        self.bookPage = 0
        self.bookRating = 0
        self.newBook = None

    def _reset(self):
        self.bookTitle = "Unknown Book"
        self.bookAuthor = "Unknown"
        self.picturePath = "resources/image/Book.png"
        self.bookPage = 0
        self.bookRating = 0
        self.newBook = None

    def createBook(self):
        self.newBook = BookEntry(None, self.bookTitle, self.bookAuthor, self.picturePath, self.bookPage, self.bookRating)


    def launch_creator(self):
        bookCreator = BookCreatorDialog()
        success = bookCreator.exec()

        if (BookCreatorDialog.DialogCode.Accepted == success):
            self.bookTitle = bookCreator.bookTitle.text()
            self.bookAuthor = bookCreator.bookAuthor.text()
            self.bookPage = bookCreator.bookPage.text()
            self.bookRating = bookCreator.bookRating.text()
            self.createBook()
            self.created.emit()
        
        self._reset()
    