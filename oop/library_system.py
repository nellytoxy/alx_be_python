class Book:
    def __init__(self,title,author):
        self.title = title
        self.author = author

class EBook(Book):
    def __init__(self, title, author, file_size):
        super().__init__(title, author)
        self.file_size = file_size

class PrintBook(Book):
    def __init__(self,title,author,page_count):
        super().__init__(title,author)
        self.page_count = page_count

class Library:
    def __init__(self):
        self.books = []
    def __str__(self):
        pass

    def add_book(self, book):
        self.books.append(book)

    def list_books(self):
        print("print details of each book")
        for book in self.books:
            if isinstance(book, Book):
                book_type = "Book"
                if isinstance(book, EBook):
                    book_type = "EBook"
                elif isinstance(book, PrintBook):
                    book_type = "PrintBook"
                print(f"{book_type}: {book.title} by {book.author}")
                if isinstance(book, EBook):
                    print(f"   File size: {book.file_size} MB")
                elif isinstance(book, PrintBook):
                    print(f"   Page count: {book.page_count}")