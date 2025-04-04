from Book_class import Book
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
    Book.load_count_of_books()

    print("~-"*30)
    print("Welcome To Your Personal Library")
    print("~-"*30)
    time.sleep(0.6)
    
    call_main_menu = True
    while call_main_menu:
        user_action = menus.main_menu()
        actions.execute_user_action(user_action)
        continue_actions = input("\nBack to Main Menu (y) or Exit Library (n)? ").lower()
        if continue_actions == "y":
            continue
        else:
            call_main_menu = False
            Book.save_count_of_books()
            sys.exit("\nGoodbye! See you soon!")

#TODO - exceptions, save on terminate.


if __name__ == "__main__":
    main()