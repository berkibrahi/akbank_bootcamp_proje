class Library:
    def __init__(self):
        self.file = open("books.txt", "a+")

    def __del__(self):
        self.file.close()

    def list_books(self):
        self.file.seek(0)
        books = self.file.readlines()
        if not books:
            print("No books found.")
        else:
            print("Books in the library:")
            for book in books:
                book_info = book.strip().split(',')
                print(f"Title: {book_info[0]}, Author: {book_info[1]}")

    def add_book(self):
        title = input("Enter the title of the book: ")
        author = input("Enter the author of the book: ")
        release_year = input("Enter the release year of the book: ")
        pages = input("Enter the number of pages of the book: ")
        book_info = f"{title},{author},{release_year},{pages}\n"
        self.file.write(book_info)
        print("Book added successfully.")

    def remove_book(self):
        title = input("Enter the title of the book you want to remove: ")
        self.file.seek(0)
        books = self.file.readlines()
        updated_books = []
        removed = False
        for book in books:
            if title in book:
                removed = True
            else:
                updated_books.append(book)
        if not removed:
            print("Book not found.")
        else:
            self.file.seek(0)
            self.file.truncate()
            self.file.writelines(updated_books)
            print("Book removed successfully.")


# Creating Library object
lib = Library()

# Menu
while True:
    print("\n*** MENU ***")
    print("1) List Books")
    print("2) Add Book")
    print("3) Remove Book")
    print("q) Quit")
    choice = input("Enter your choice: ")

    if choice == '1':
        lib.list_books()
    elif choice == '2':
        lib.add_book()
    elif choice == '3':
        lib.remove_book()
    elif choice == 'q':
        break
    else:
        print("Invalid choice. Please try again.")
