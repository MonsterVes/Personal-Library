class Book:

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
        self.format = format
        self.price = price
        self.purchase_date = purchase_date
        self.status = status
        self.personal_rating = personal_rating
        self.notes = notes


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
        return self.__dict__
    

