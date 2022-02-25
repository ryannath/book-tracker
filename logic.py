import fileinput
import pickle
from typing import Dict
from datastruct.book import Book
from terminal.printer import Printer
# Load data of read books

try:
    with open("library.bt", "rb") as f:
        print("Loading")
        data = pickle.load(f)
except Exception as e:
    print(e)
    data: Dict[str, Book] = {}

Printer.clear()
Printer.print_help_info()

while True:
    line = Printer.get_input().lower()
    
    if line == "q":
        break

    elif line == "new" or line == "n":
        title = input("Book Title: ")
        new_book = Book(title)
        data[title] = new_book

    elif line == "pa" or line == "print all":
        for book in data.values():
            print(book)

    elif line == "?" or line == "h" or line == "help":
        Printer.print_help_info()
    
    elif line == "c" or line == "clear":
        Printer.clear()
    
    elif line =="save":
        with open('library.bt', 'wb') as db:
            
            pickle.dump(data, db)

    else:
        print("Unknown command, type ? to see available commands")

