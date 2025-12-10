from list_of_books import *
while True:
    class library:
        def __init__(self, name, location, phonenumber, books_max):
            self.name = name
            self.location = location
            self.phonenumber = phonenumber
            self.books_max = books_max
            print(f"\nLibrary Name:{self.name}\nLocation:{self.location}\nContact Number:{self.phonenumber}\nAvailaable Books:{self.books_max}")

    hazara = library("Hazara Library", "College Road", "031189811", "More than 2000")

    a=print("\na-borrow a book.")
    b=print("b-return a book.")
    c=print("c-Exit.")
    option=(input("\nEnter your option:"))
    if (option=="a"):
        class issued_Book:
            def __init__(self, title, author, genre, issued_to):
                self.name = title
                self.author = author
                self.genre = genre
                self.buyer = issued_to
                Name=input("\nEnter your Name  :")
                book=input("Enter the Book Name:")
                if book in famous_books_dict:
                    author=famous_books_dict[book]
                    print("book is borrowed succesfully.")
                    print(f"\nTitle   : {book}\nAuthor : {author}")
                    print(f"Issued_To : {Name}")       
                else:
                    print("book is not present")

        uzair=issued_Book("book", "Author","Novel","person")
        
    elif(option=="b"):
        class return_book:
            def __init__(self,name,author,returned_by):
                self.title=name
                self.author=author
                self.recieved=returned_by
                Name=input("\nEnter your Name  :")
                book=input("Enter the Book Name you return:")
                if book in famous_books_dict:
                    author=famous_books_dict[book]
                    print("book is returned successfully")
                    print(f"\nTitle   : {book}\nAuthor : {author}")
                    print(f"Reyurned_by : {Name}") 
        uzair=return_book("book", "Author","person")
        
    elif(option=="c"):
        break
        
           


        


           
           