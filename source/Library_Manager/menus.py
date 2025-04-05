import time
import pyinputplus as pyip


def main_menu():
    """
    Prints the Main menu where the available actions are listed. Prompts the user to chose an action and returns the value. 
    The value is later used in 'main.py' in order to execute the action according to the 'action.execute_user_action' function
    """

    print("\nPlease choose an action:\n\n~-~-~ 1. View Books   ~-~-~\n~-~-~ 2. Search Book  ~-~-~")
    print("~-~-~ 3. Manage Books ~-~-~\n~-~-~ 4. Statistics   ~-~-~\n~-~-~ 5. Exit Library ~-~-~\n")
    user_action = pyip.inputChoice(["1","2","3","4","5"], prompt = "Your choice (1-5): \n")
    return user_action


def sub_menu():
    """
    Prints the Sub menu from option 3 in Main menu (3. Manage Books) where the available actions are listed. 
    Prompts the user to chose an action and returns the value. 
    The value is later used in 'main.py' in order to execute the action according to the 'action.execute_user_action' function"""

    print("~-"*30)
    print("3. Manage Books")
    print("~-"*30)
    time.sleep(0.6)
    print("\nPlease choose an action:\n\n~-~-~ 1. Add Book    ~-~-~\n~-~-~ 2. Edit Book   ~-~-~")
    print("~-~-~ 3. Delete Book ~-~-~\n~-~-~ 4. Main Menu   ~-~-~\n")
    user_action = pyip.inputChoice(["1","2","3","4"], prompt = "Your choice (1-4): \n")
    return user_action
    


