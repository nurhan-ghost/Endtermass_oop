from functools import reduce
class Book:
    def __init__(self, book_id, title, price, available):
        self.book_id = book_id
        self.title = title
        self.price = price
        self.available = available

    def __str__(self):
        return f"ID: {self.book_id}, Title: {self.title}, Price: ₸{self.price:.2f}, Available: {'Yes' if self.available else 'No'}"

    def toggle_availability(self):
        if self.available:
            self.available = False
        else:
            self.available = True

class EBook(Book):
    def __init__(self, book_id, title, price, available, file_size):
        super().__init__(book_id, title, price, available)
        self.file_size = file_size

    def __str__(self):
        return super().__str__() + f", File Size: {self.file_size}MB"

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print(f"Book \"{book.title}\" added.")

    def borrow_book(self, book_id):
        book = None
        for b in self.books:
            if b.book_id == book_id and b.available:
                 book = b
                 break
        if book:
            book.toggle_availability()
            print(f"Book \"{book.title}\" borrowed.")
        else:
            print("Book unavailable or invalid ID.")

    def return_book(self, book_id):
        book = None
        for b in self.books:
           if b.book_id == book_id and not b.available:
                book = b
                break
        if book:
            book.toggle_availability()
            print(f"Book \"{book.title}\" returned.")
        else:
            print("Book not borrowed or invalid ID.")

    def display_books(self):
        if self.books:
            for book in self.books:
                print(book)
        else:
            print("No books in the library.")

    def sort_books_by_price(self, ascending=True):
        self.books.sort(key=lambda b: b.price, reverse=not ascending)
        print(f"Books sorted by price ({'ascending' if ascending else 'descending'}):")
        self.display_books()

    def calculate_total_value(self):
        total_value = reduce(lambda acc, b: acc + b.price, self.books, 0)
        print(f"Total value of books: ${total_value:.2f}")


def get_input(inp, input_type=str):
    return input_type(input(inp))


def main():
    library = Library()

    while True:
        print("\nMenu:")
        print("1. Add a book")
        print("2. Display books")
        print("3. Borrow a book")
        print("4. Return a book")
        print("5. Total value of books")
        print("6. Sort books by price")
        print("7. Exit")

        choice = input("\nYour choice: ")

        if choice == "1":
            try:
                book_id = get_input("Enter book ID: ", int)
                title = input("Enter book title: ")
                price = get_input("Enter book price: ", float)
                available = input("Available (yes/no): ").strip().lower() == "yes"
                book_type = input("Is this an EBook? (yes/no): ").strip().lower()

                if book_type == "yes":
                    file_size = float(input("Enter file size (MB): ").strip()) 
                    library.add_book(EBook(book_id, title, price, available, file_size))
                else:
                    library.add_book(Book(book_id, title, price, available))
            except ValueError:
                print("Error adding book. Please provide valid inputs.") 

        elif choice == "2":
            library.display_books()

        elif choice == "3":
            try:
                book_id = get_input("Enter book ID to borrow: ", int)
                library.borrow_book(book_id)
            except:
                print("Error: Invalid ID format")

        elif choice == "4":
            try:
                book_id = int(input("Enter book ID to return: ").strip())
                library.return_book(book_id)
            except ValueError:
                print("Invalid ID format.")

        elif choice == "5":
            library.calculate_total_value()

        elif choice == "6":
            order = input("Sort by price (ascending/descending): ").strip().lower()
            if order == "ascending":
                library.sort_books_by_price(ascending=True)
            elif order == "descending":
                library.sort_books_by_price(ascending=False)
            else:
                print("Invalid input. Please enter 'ascending' or 'descending'.")

        elif choice == "7":
            print("Thanks. Goodbye!")
            break

        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()