  GNU nano 7.2                       library.py                                 
# -------------------------------------------
# CREATED: 170626 19:40 PM GMT
# UPDATED: 170626 19:40 PM GMT
# -------------------------------------------
# This code borrowed from:
# https://www.youtube.com/shorts/MAnba0zEWu4
# -------------------------------------------

# Real world example

class Book:
    def __init__(self,title,author):
        self.title=title
        self.author=author

class Library:
    def __init__(self):
        self.books=[]
    def add_book(self,book):
        self.books.append(book)
    def display_books(self):
        for book in self.books:
            print(f"{book.title} by {book.author}")

# Adding books to the library

library=Library()
library.add_book(Book("1984","George Orwell"))
library.add_book(Book("To Kill a mocking bird","Harper Lee"))
library.display_books()
