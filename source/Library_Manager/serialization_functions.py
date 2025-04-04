import json
import os
from Book_class import DATA_PATH


def add_to_json_book_file(book):
    """
    Function that adds the book info to a JSON file where all the books will be stored
    """
    try:
        filename = "Book_library.json"
        file_path = os.path.join(DATA_PATH, filename)
        
        if not os.path.isdir(DATA_PATH):
                os.mkdir(DATA_PATH)
        with open(file_path, "r") as file:
            book_data = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        book_data = {"Books": []}
        
    except Exception:
        print("Ups.. Something went wrong")

    # book_data[book.title] = book.to_dict()
    book_data["Books"].append(book.to_dict())
    with open(file_path, "w") as file:
        json.dump(book_data, file, indent=4)

    print("-~" * 25)
    print(f"{book.title} has been added to the Library")
    print("-~" * 25)


# def get_from_json_book_file(book, file_name="Book_library.json"):
