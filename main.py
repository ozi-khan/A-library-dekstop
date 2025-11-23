from list_of_books import *
class library:
    def __init__(self, name, location, phonenumber, books_max):
        self.name = name
        self.location = location
        self.phonenumber = phonenumber
        self.books_max = books_max
        print(f"\nLibrary Name:{self.name}\nLocation:{self.location}\nContact Number:{self.phonenumber}\nAvailaable Books:{self.books_max}")

hazara = library("Hazara Library", "College Road", "031189811", "More than 2000")

class Book:
    def __init__(self, title, author, genre, issued_to):
        self.name = title
        self.author = author
        self.genre = genre
        
        self.buyer = issued_to
        print("\nPrecaution ! The author name must be in tile form or either copied from Google.")
        Name=input("\nEnter your Name  :")
        book=input("Enter the Book Name:")
        if book in famous_books_dict:
            author=famous_books_dict[book]
            print(f"\nTitle   : {book}\nAuthor : {author}")
            print(f"Issued_To : {Name}")       
        else:
            print("book is not present")


uzair=Book("book", "Author","Novel","person")


           
           