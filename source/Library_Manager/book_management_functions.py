from Book_class import Book
import pyinputplus as pyip
import json
import os
import menus

DATA_PATH = "../Data_files"
filename = "Book_library.json"
FILE_PATH = os.path.join(DATA_PATH, filename)


class Book_Manager:
    def __init__(self):
        try:
            if not os.path.isdir(DATA_PATH):
                os.mkdir(DATA_PATH)

            if os.path.exists(FILE_PATH):
                with open(FILE_PATH,"r") as file:
                    books_from_file = json.load(file)
                    self.view_books = books_from_file["Books"]
            else:
                self.view_books = []
                with open(FILE_PATH, "w") as file:
                    json.dump( self.view_books, file, indent=4)
        except FileNotFoundError as e:
            print(f"File not found: {e}. Please try again.")
            books_from_file = {"Books": []}
        except json.JSONDecodeError as e:
            print(f"Error decoding JSON: {e}. Please check the file format.")
            books_from_file = {"Books": []}
        except Exception as e:
            print(f"An error occurred: {e}. Please try again.")


    def save_books_on_exit(self):
        with open(FILE_PATH, "w") as file:
            json.dump({"Books": self.view_books}, file, indent=4)


    def books_total_cost(self):
        total_price = 0
        for book in self.view_books:
            total_price += book["price"]
        return total_price
    

    def books_count(self):
        return len(self.view_books)
    

    def add_book(self):
        """
        ADD BOOK TO LIBRARY
        Gather book info input from the user to add as Book instance attributes. Create a new_book instance of the Book object 
        and add it to the Book_library.json file.
        """
        print("\n~-~-~ Please enter book info: ~-~-~")
        while True:
            try:
                # Gather input
                title = input("Enter book title: ").title()
                author = input("Enter author name: ").title()
                isbn = pyip.inputNum("Enter ISBN: " )
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
                    print("\n***Invalid purchase date.***\n Purchase date is prior to Publishing year. Please re-enter book info.\n")
                    continue
                status = pyip.inputChoice(["Read", "Want to read", "In progress", "Unread"], 
                                        prompt = "Enter read status (Read, Want to read, In progress, Unread): ").capitalize()
                personal_rating = pyip.inputChoice(["1","2","3","4","5", "N/A"], prompt = "Enter personal rating (1-5 or N/A): ").upper()
                notes = input("Enter any additional notes: ")

                # Initialize new book object 
                new_book = Book(title, author, isbn, year, publisher, genre, pages, format, price, 
                        purchase_date, status, personal_rating, notes)
                
                # Add the new book to the Book_library.json file
                self.view_books.append(new_book.to_dict())
                break

            except ValueError as e:
                print(f"Invalid input: {e}. Please try again.")
            except Exception as e:
                print(f"An error occurred: {e}. Please try again.")
        print("-~" * 25)
        print(f"{title} has been added to the Library")
        print("-~" * 25)


    def view_library(self):
        """
        VIEW BOOKS IN LIBRARY
        List all books by title and authir from Book_library.json file. Gives the total count of books that are currently in the library.
        """
        
        print("\n~-~-~ Books in Library: ~-~-~\n")
        try:
            for book in self.view_books:
                print(f"'{book["title"]}' by {book["author"]}")
            print(f"\nTotal Books in Library: {self.books_count()}\n")
        except TypeError:
            print("There are no books in the Library")

    def search_book(self,book_title):
        """
        SEARCH FOR A BOOK IN LIBRARY
        Searches by book title in titles in Book_Library.json .If book is found in Book_library.json file, 
        the function prints book info.
        """
        print("\n~-~-~ Search Results: ~-~-~\n")
        try:
            is_found = False
            for book in self.view_books:
                if book_title.lower() in book["title"].lower():
                    for key, value in book.items():
                        print(f"{key.capitalize()}: {value}")
                    is_found = True
                    break
            if not is_found:
                print(f"Can't find '{book_title}' in Personal Library")

        except Exception as e:
            print(f"An error occurred: {e}. Please try again.")    


    def delete_book(self):
        """
        DELETE FOR A BOOK IN LIBRARY
        Searched by book title in titles in Book_Library.json .If book is found in Book_library.json file, 
        the function deletes the book.
        """
        try:
            book_to_delete = input("Enter the title of the book you want to delete: ")
            is_found = False
            for book in self.view_books:
                if book["title"] == book_to_delete:
                    confirm_deletion = input(f"\nAre you sure you want to delete *{book["title"]}* by {book["author"]} from PersonalLibrary? (Yes/No): ").lower()
                    if confirm_deletion == "yes":
                        self.view_books.remove(book)
                        is_found = True
                        print("-~" * 25)
                        print(f"{book_to_delete} has been removed from the Library")
                        print("-~" * 25) 
                        break 
                    else:
                        menus.sub_menu()
            if not is_found:
                print(f"\nCan't find {book_to_delete} in Personal Library\n")
        except Exception as e:
            print(f"An error occurred: {e}. Please try again.")
            

    def edit_book(self):
        """
        EDIT BOOK PROPERTY IN LIBRARY
        Searched by book title in titles in Book_Library.json .If book is found in Book_library.json file the functions prints it and asks for an attribute to be changed. 
        If the attribute is found, the function changes it with the new inputet value.
        """
        while True:
            try:
                book_to_edit = input("\nEnter the title of the book you want to edit: ")
                is_found = False
                for book in self.view_books:
                    if book_to_edit.lower() in book["title"].lower():
                        is_found = True
                        attr_to_edit = input("\nWhich property would you like to edit? ").lower()
                        if attr_to_edit in book:
                            if attr_to_edit == "isbn":
                                new_value = pyip.inputNum(f"Enter the new value for {attr_to_edit}: ")
                            elif attr_to_edit == "year":
                                date = pyip.inputDate(f"Enter the new value for {attr_to_edit}: ", formats = ["%Y-%m-%d"])
                                new_value = date.strftime("%Y-%m-%d")
                            elif attr_to_edit == "purchase date":
                                date = pyip.inputDate(f"Enter the new value for {attr_to_edit}: ", formats = ["%Y-%m-%d"])
                                new_value = date.strftime("%Y-%m-%d")
                            elif attr_to_edit == "pages":
                                new_value = pyip.inputInt(f"Enter the new value for {attr_to_edit}: ", min=3)
                            elif attr_to_edit == "genre":
                                new_value = pyip.inputMenu(["Action", "Adventure", "Children", "Comedy", "Crime", "Drama", "Fantasy", 
                                                "Historical", "Mystery", "Poetry", "Science", "Sci-Fi"], numbered = True, prompt = f"Enter the new value for {attr_to_edit}: ").capitalize()
                            elif attr_to_edit == "format":
                                new_value = pyip.inputChoice(["Paperback", "Hardcover", "E-book", "Audiobook"], prompt = f"Enter the new value for {attr_to_edit}: ")
                            elif attr_to_edit == "status":
                                new_value = pyip.inputChoice(["Read", "Want to read", "In progress", "Unread"], prompt = f"Enter the new value for {attr_to_edit}: ").capitalize()
                            elif attr_to_edit == "price":
                                new_value = pyip.inputFloat(f"Enter the new value for {attr_to_edit}: ", min = 0.1)
                            elif attr_to_edit == "personal rating":
                                new_value = pyip.inputChoice(["1","2","3","4","5", "N/A"], prompt = f"Enter the new value for {attr_to_edit}: ").upper()
                            elif attr_to_edit:
                                new_value = input(f"Enter the new value for {attr_to_edit}: ").capitalize()
                            else:
                                new_value = input(f"Enter the new value for {attr_to_edit}: ").capitalize()
                            
                            book[attr_to_edit] = new_value
                            print(f"\n{attr_to_edit.capitalize()} has been updated successfully.\n")
                            break
                        else:
                            print(f"\nInvalid property: {attr_to_edit}. Please try again.\n")
                            break
                
                if not is_found:
                    print(f"\nCan't find '{book_to_edit}' in Personal Library.\n")
                    menus.sub_menu()

                continue_editing = input("Do you want to edit another book? (y/n): ").lower()
                if continue_editing != "y":
                    break

            except Exception as e:
                print(f"An error occurred: {e}. Please try again.")