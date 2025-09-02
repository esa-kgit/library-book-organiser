class Library:

    def __init__(self):
        self.currentbooks = []

    class Book:

        def __init__(self, title, author):
            self.title = title
            self.author = author
            self.reviews = []
            

        def add_review(self, reviewer, txt):
            newreview = self.Review(reviewer, txt)
            self.reviews.append(newreview)

        class Review:

            def __init__(self, reviewer, txt):
                self.reviewer = reviewer
                self.txt = txt

    def print_books(self):
        for book in self.currentbooks:
            print(f'Title: {book.title}, Author: {book.author}')
            if book.reviews:
                print(' Reviews:')
                for review in book.reviews:
                    print(f'    -{review.reviewer}: {review.txt}')
            if self.currentbooks[-1] != book:
                print(' ')
                

    def add_book(self, title, author):
        book = self.Book(title, author)
        self.currentbooks.append(book)

# test block

lib = Library()
lib.add_book("1984", "George Orwell")
lib.add_book("Brave New World", "Aldous Huxley")

lib.currentbooks[0].add_review("Alice", "A chilling dystopia.")
lib.currentbooks[0].add_review("Bob", "Very thought-provoking.")
lib.currentbooks[1].add_review("Charlie", "A classic!")

lib.print_books()