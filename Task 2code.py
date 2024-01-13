class Book:
    def __init__(self, book_id, title, author):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.is_available = True

    def borrow(self, member):
        if self.is_available:
            self.is_available = False
            self.borrower = member
            member.borrowed_books.append(self)
            print(f"{member.name} borrowed {self.title}")
        else:
            print("Book is not available.")

    def return_book(self):
        self.is_available = True
        self.borrower = None
        print(f"{self.title} has been returned.")

    def __str__(self):
        return f"Book ID: {self.book_id}, Title: {self.title}, Author: {self.author}, Available: {self.is_available}"


class LibrarySystem:
    def __init__(self, name):
        self.name = name
        self.books = []
        self.members = []

    def add_book(self, title, author):
        book_id = len(self.books) + 1
        book = Book(book_id, title, author)
        self.books.append(book)
        return book

    def add_member(self, name):
        member_id = len(self.members) + 1
        member = Member(member_id, name)
        self.members.append(member)
        return member

    def display_available_books(self):
        available_books = [book for book in self.books if book.is_available]
        if not available_books:
            print("No books available in the library.")
        else:
            for book in available_books:
                print(book)

    def find_book(self, title):
        for book in self.books:
            if book.title == title:
                return book
        return None

    def borrow_book(self, member, title):
        book = self.find_book(title)
        if book:
            book.borrow(member)
        else:
            print("Book not found.")

    def return_book(self, title):
        book = self.find_book(title)
        if book:
            book.return_book()
        else:
            print("Book not found.")

    def __str__(self):
        return f"Library System: {self.name}, Number of Books: {len(self.books)}, Number of Members: {len(self.members)}"


class Member:
    def __init__(self, member_id, name):
        self.member_id = member_id
        self.name = name
        self.borrowed_books = []

    def borrow_book(self, book):
        if book.is_available:
            book.borrow(self)
            return True
        else:
            print("Book is not available for borrowing.")
            return False

    def return_book(self, book):
        if book in self.borrowed_books:
            book.return_book()
            return True
        else:
            print("You did not borrow this book from the library.")
            return False

    def __str__(self):
        return f"Member ID: {self.member_id}, Name: {self.name}, Borrowed Books: {len(self.borrowed_books)}"
        
# Example usage:
library_system = LibrarySystem("City Library")
# Add books to the library
book1 = library_system.add_book("Wings of Fire", "A P J Abdul Kalam")
book2 = library_system.add_book("Mahabharata: The Great Indian Epic", "Sudharshan Ray")
book3 = library_system.add_book("Harry Potter and Chamber of Secrets", "J K Rowling")
# Add members to the library
member1 = library_system.add_member("Deepu")
member2 = library_system.add_member("Jhonny")

# Display available books
print("Available Books:")
library_system.display_available_books()
# Borrow a book
member1.borrow_book(book1)
# Display available books after borrowing
print("\nAvailable Books after borrowing:")
library_system.display_available_books()
# Display library information
print("\nLibrary Information:")
print(library_system)
# Return a book
member1.return_book(book1)
print("\nAvailable Books after returning:")
library_system.display_available_books()
