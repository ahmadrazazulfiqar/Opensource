class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.checked_out = False

    def check_out(self):
        if not self.checked_out:
            self.checked_out = True
            return f"Checked out: {self.title} by {self.author}"
        else:
            return f"{self.title} is already checked out."

    def return_book(self):
        if self.checked_out:
            self.checked_out = False
            return f"Returned: {self.title} by {self.author}"
        else:
            return f"{self.title} is not checked out."


class Library:
    def __init__(self, name):
        self.name = name
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def list_books(self):
        print(f"Available books in {self.name}:")
        for book in self.books:
            if not book.checked_out:
                print(f"{book.title} by {book.author}")

    def remove_book(self, title):
        for book in self.books:
            if title.lower() in book.title.lower():
                self.books.remove(book)
                return f"Removed: {book.title} by {book.author}"
        return f"Book not found: {title}"


class MemberLibrary(Library):
    def __init__(self, name):
        super().__init__(name)
        self.members = {}

    def register_member(self, member_name):
        if member_name not in self.members:
            self.members[member_name] = []

    def view_checked_out_books(self, member_name):
        if member_name in self.members:
            checked_out_books = self.members[member_name]
            if checked_out_books:
                print(f"{member_name}'s checked-out books:")
                for book in checked_out_books:
                    print(f"{book.title} by {book.author}")
            else:
                print(f"{member_name} has no books checked out.")
        else:
            print(f"{member_name} is not a registered member of {self.name}.")

    def check_out_book(self, member_name, title):
        if member_name in self.members:
            for book in self.books:
                if title.lower() in book.title.lower() and not book.checked_out:
                    self.members[member_name].append(book)
                    return f"{member_name} checked out: {book.title} by {book.author}"
            return f"{member_name} cannot check out {title}. The book is already checked out or not available."
        else:
            return f"{member_name} is not a registered member of {self.name}."

    def return_book(self, member_name, title):
        if member_name in self.members:
            for book in self.members[member_name]:
                if title.lower() in book.title.lower():
                    self.members[member_name].remove(book)
                    book_status = book.return_book()
                    return f"{member_name} returned: {book_status}"
            return f"{member_name} does not have {title} checked out."
        else:
            return f"{member_name} is not a registered member of {self.name}"


# Demonstration
if __name__ == "__main__":
    # Create a library object.
    library = MemberLibrary("My Library")

    # Add several books to the library.
    book1 = Book("The Great Gatsby", "F. Scott Fitzgerald")
    book2 = Book("To Kill a Mockingbird", "Harper Lee")
    book3 = Book("1984", "George Orwell")

    library.add_book(book1)
    library.add_book(book2)
    library.add_book(book3)

    # View the list of available books.
    library.list_books()

    # Remove a book from the library.
    print(library.remove_book("To Kill a Mockingbird"))

    # Create a member library object.
    library.register_member("Alice")

    # Allow a member to check out a book from the library and display their checked-out books.
    print(library.check_out_book("Alice", "The Great Gatsby"))
    library.view_checked_out_books("Alice")

    # Allow the member to return a book to the library.
    print(library.return_book("Alice", "The Great Gatsby"))
    library.view_checked_out_books("Alice")
