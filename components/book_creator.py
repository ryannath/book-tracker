# from PyQt6.QtWidgets impor
from PyQt6.QtCore import pyqtSignal
from PyQt6.QtWidgets import QWidget

from components.book_creator_dialog import BookCreatorDialog
from components.book_entry import BookEntry
from datastruct.book import Book

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

    def reset(self):
        self.bookTitle = "Unknown Book"
        self.bookAuthor = "Unknown"
        self.picturePath = "resources/image/Book.png"
        self.bookPage = 0
        self.bookRating = 0
        self.newBook = None

    def createBook(self, book:Book=None):
        if not book:
            self.newBook = BookEntry(self.bookTitle, self.bookAuthor, self.picturePath, self.bookPage, self.bookRating)
        else:
            self.newBook = BookEntry(book)

    def launch_creator(self):
        bookCreator = BookCreatorDialog()
        success = bookCreator.exec()

        if (BookCreatorDialog.DialogCode.Accepted == success):
            if (bookCreator.bookTitle.text()):
                self.bookTitle = bookCreator.bookTitle.text()
            if (bookCreator.bookAuthor.text()):
                self.bookAuthor = bookCreator.bookAuthor.text()
            if (bookCreator.bookPage.text()):
                self.bookPage = bookCreator.bookPage.text()
            if (bookCreator.bookRating.text()):
                self.bookRating = bookCreator.bookRating.text()

            self.createBook()
            self.created.emit()
        
        self.reset()
    