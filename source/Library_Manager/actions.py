from Book_class import Book
import book_management_functions as bm
import menus
import sys


def execute_user_action(action):
    """
    Executes a specific action based on the user's input.
    Parameters:
        action (str): The user's selected action, represented as a string.
    Actions:
        - "1": View the library by calling the `view_library` method.
        - "2": Search for a book by title. Prompts the user for input and calls the `search_book` method.
        - "4": Displays a message indicating that the "Statistics" functionality is under construction.
        - "5": Saves the count of books using the `save_count_of_books` method and exits the program.
        - Other ("3"): Displays a sub-menu for additional actions:
            - "1": Adds a new book by calling the `add_book` method.
            - "2": Displays a message indicating that the "Edit Book" functionality is under construction.
            - "3": Displays a message indicating that the "Delete Book" functionality is under construction.
            - "4": Returns to the main menu by calling the `main_menu` method.
    Note:
        This function relies on external modules and methods such as `bm.view_library`, 
        `bm.search_book`, `Book.save_count_of_books`, and `menus.main_menu`.
    """

    if action == "1":
        bm.view_library()
    elif action == "2":
        search_book = input("\nEnter book title you are searching for: ")
        bm.search_book(search_book)
    elif action == "4":
        print("\n*Statistics* functionality is under construction")
    elif action == "5":
        Book.save_count_of_books()
        sys.exit("\nGoodbye! See you soon!")
    else:
        sub_action = menus.sub_menu()
        if sub_action == "1":
            bm.add_book()
        elif sub_action == "2":
            print("\n*Edit Book* functionality is under construction")
        elif sub_action == "3":
            bm.delete_book()
        elif sub_action == "4":
            menus.main_menu()
        