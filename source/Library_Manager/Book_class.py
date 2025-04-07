import os
import json


DATA_PATH = "../Data_files"
count_of_books = "Count_of_books.json"
file_path = os.path.join(DATA_PATH, count_of_books)

class Book:
    count_of_books = 0

    @classmethod
    def load_count_of_books(cls):
        try:
            with open(file_path, "r") as file:
                cls.count_of_books = json.load(file)
        except FileNotFoundError:
            cls.count_of_books = 0

    @classmethod
    def save_count_of_books(cls):
        with open(file_path, "w") as file:
            json.dump(cls.count_of_books, file)


    def __init__(self, title, author, isbn, year, publisher, genre, pages, format, price, purchase_date,
                status, personal_rating, notes
                ):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.year = year
        self.publisher = publisher
        self.genre = genre
        self.pages = pages
        self._format = format
        self.price = price
        self.purchase_date = purchase_date
        self._status = status
        self._personal_rating = personal_rating
        self.notes = notes

        # Book.count_of_books += 1
        # Book.save_count_of_books()


    def __str__(self):
        return (
            f"Title: {self.title}\n"
            f"Author: {self.author}\n"
            f"ISBN: {self.isbn}\n"
            f"Publishing year: {self.year}\n"
            f"Publisher: {self.publisher}\n"
            f"Genre: {self.genre}\n"
            f"Pages: {self.pages}\n"
            f"Format: {self.format}\n"
            f"Price EUR: {self.price}\n"
            f"Purchase date: {self.purchase_date}\n"
            f"Status: {self.status}\n"
            f"Personal rating: {self.personal_rating}\n"
            f"Notes: {self.notes}\n"
        )

    def to_dict(self):
        return {
            "title": self.title,
            "author": self.author,
            "isbn": self.isbn,
            "year": self.year,
            "publisher": self.publisher,
            "genre": self.genre,
            "pages": self.pages,
            "format": self.format,
            "price": self.price,
            "purchase date": self.purchase_date,
            "status": self.status,
            "personal rating": self.personal_rating,
            "notes": self.notes
        }

    """Checks for allowed Personal ratings"""

    @property
    def personal_rating(self):
        return self._personal_rating

    @personal_rating.setter
    def personal_rating(self, personal_rating):
        if personal_rating not in ["1", "2", "3", "4", "5", "N/A"]:
            raise ValueError("Invalid rating. Allowed ratings: 1, 2, 3, 4, 5")
        self._personal_rating = personal_rating

    """Check for allowed book formats"""

    @property
    def format(self):
        return self._format

    @format.setter
    def format(self, format):
        if format not in ["Paperback", "Hardcover", "E-book", "Audiobook"].lower():
            raise ValueError(
                "Invalid Format. Allowed formats: Paperback, Hardcover, E-book, Audiobook"
            )
        self._format = format

    """Check for allowed Personal read statuses"""

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, status):
        if status not in ["Read", "Want to read", "In progress", "Unread"].lower():
            raise ValueError(
                "Invalid read status. Allowed statuses: Read, Want to read, In progress, Unread"
            )
        self._status = status


# book1 = Book("Dune", "Frank Herbert", "0441172717", "1990-09-01", "Ace", "Sci-fi", "896", "Paperback", "7.52",
#                  "2001-12-10", "5", "Read", "Great Sci-Fi book")
# book2 = Book("Dune the messiah", "Frank Herbert", "0441172718", "1995-09-01", "Ace", "Sci-fi", "263", "Paperback", "5.42",
#                  "2001-12-10", "4", "Read", "Sequel to Dune. Not horrible")
