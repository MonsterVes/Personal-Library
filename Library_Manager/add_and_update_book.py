from book import Book
from serialization_functions import add_to_json_book_file
import pyinputplus as pyip


def add_book():

    """
    Gather book info input from the user in order to create a new Book object and add it to the Book_library.json file
    """
    while True:
        try:
            # Gather input
            title = input("Enter book title: ").title()
            author = input("Enter author name: ").title()
            isbn = pyip.inputNum("Enter ISBN: ", )
            year_obj = pyip.inputDate("Enter publishing year (YYYY-MM-DD): ", formats = ["%Y-%m-%d"])
            year = year_obj.strftime("%Y-%m-%d")
            publisher = input("Enter publisher name: ").capitalize()
            # Select a genre from a menu list
            print("Enter book genre: ")
            genre = pyip.inputMenu(["Action", "Adventure", "Children", "Comedy", "Crime", "Drama", "Fantasy", 
                                    "Historical", "Mystery", "Poetry", "Science", "Sci-Fi"], numbered = True).capitalize()
            pages = pyip.inputInt("Enter number of pages: ", min=3)
            format = pyip.inputChoice(["Paperback", "Hardcover", "E-book", "Audiobook"], 
                                      prompt = "Enter book format (Paperback, Hardcover, E-book, Audiobook): ").capitalize()
            price = pyip.inputFloat("Enter book price: ", min = 0.1)
            # Validate purchase date is after the publishing date
            purchase_date_obj = pyip.inputDate("Enter date of purchase (YYYY-MM-DD): ", formats = ["%Y-%m-%d"])
            if purchase_date_obj > year_obj:
                purchase_date = purchase_date_obj.strftime("%Y-%m-%d")
            else:
                # Start from the begining in case the publishing year has been inputet with an error.
                print("Invalid purchase date. Purchase date is prior to Publishing year. Please re-enter book info.")
                continue
            personal_rating = pyip.inputChoice(["1","2","3","4","5", "N/A"], prompt = "Enter personal rating (1-5 or N/A): ")
            status = pyip.inputChoice(["Read", "Want to read", "In progress", "Unread"], 
                                      prompt = "Enter read status (Read, Want to read, In progress, Unread): ").capitalize()
            notes = input("Enter any additional notes: ")

            # Initialize new book object 

            new_book = Book(title, author, isbn, year, publisher, genre, pages, format, price, 
                    purchase_date, personal_rating, status, notes)
            
            # Add the new book to the Book_library.json file

            add_to_json_book_file(new_book)
            break

        except ValueError as e:
            print(f"Invalid input: {e}. Please try again.")
        except Exception as e:
            print(f"An error occurred: {e}. Please try again.")


add_book()

