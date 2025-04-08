from book_management_functions import Book_Manager
import menus
import actions
import time
import sys


def main():
    """
    The main function serves as the entry point for the Personal Library application.
    It initializes the library by loading the count of books, displays a welcome message,
    and provides a loop for the user to interact with the main menu. The user can choose
    actions from the menu and decide whether to return to the main menu or exit the application.
    On exit, saves the count of books using the `Book.save_count_of_books` method and terminates the program.
    """


    print("~-"*16)
    print("Welcome To Your Personal Library")
    print("~-"*16)
    time.sleep(0.6)
    
    call_main_menu = True
    book_manager = Book_Manager()
    while call_main_menu:
        user_action = menus.main_menu()
        actions.execute_user_action(user_action,book_manager)
        continue_actions = input("\nBack to Main Menu (m) or Exit Library (any key)? ").lower()
        if continue_actions == "m":
            book_manager.save_books_on_exit()
            continue
        else:
            call_main_menu = False
            book_manager.save_books_on_exit()
            sys.exit("\nGoodbye! See you soon!")



if __name__ == "__main__":
    main()