class Library:
    def __init__(self):
        self.books = []

    def display_books(self):
        if not self.books:
            print("No books available.")
            return
        for book in self.books:
            print(f"Title: {book.title}, Author: {book.author}, Status: {book.status}")

    def add_book(self):
        title = input("Enter book title: ")
        author = input("Enter book author: ")
        new_book = Book(title, author)
        self.books.append(new_book)
        print(f"Book '{title}' by {author} added.")

    def lend_book(self):
        title = input("Enter the title of the book to lend: ")
        for book in self.books:
            if book.title.lower() == title.lower():
                if book.status == "Available":
                    book.status = "Borrowed"
                    print(f"Book '{title}' lent.")
                    return
                else:
                    print(f"Book '{title}' is currently borrowed.")
                    return
        print(f"Book '{title}' not found.")

    def return_book(self):
        title = input("Enter the title of the book to return: ")
        for book in self.books:
            if book.title.lower() == title.lower():
                if book.status == "Borrowed":
                    book.status = "Available"
                    print(f"Book '{title}' returned.")
                    return
                else:
                    print(f"Book '{title}' is already available.")
                    return
        print(f"Book '{title}' not found.")

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.status = "Available"

def main():
    library = Library()

    while True:
        print("\nLibrary Management System")
        print("1. Display Books")
        print("2. Add Book")
        print("3. Lend Book")
        print("4. Return Book")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            library.display_books()
        elif choice == "2":
            library.add_book()
        elif choice == "3":
            library.lend_book()
        elif choice == "4":
            library.return_book()
        elif choice == "5":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
