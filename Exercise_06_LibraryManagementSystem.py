class Library:
    def __init__(self):
        self.noBooks = 0
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        self.noBooks = len(self.books)

    def remove_book(self, book):
        self.books.remove(book)
        self.noBooks = len(self.books)

    def showInfo(self):
        print(f"The library has {self.noBooks} books")
        for book in self.books:
            print(book)


l1 = Library()
l1.add_book("Harry Potter")
l1.add_book("Mahabharat")
l1.add_book("Ramayana")
l1.remove_book("Ramayana")
l1.showInfo()
