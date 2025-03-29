import json


def add_to_json_book_file(book, file_name="Book_library.json"):
    """
    Function that adds the book info to a JSON file where all the books will be stored
    """
    try:
        with open(file_name, "r") as file:
            book_data = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        book_data = {}
    except Exception:
        print("Ups.. Something went wrong")

    book_data[book.title] = book.to_dict()

    with open(file_name, "w") as file:
        json.dump(book_data, file, indent=4)

    print("-~" * 25)
    print(f"{book.title} has been added to the Library")
    print("-~" * 25)


# def get_from_json_book_file(book, file_name="Book_library.json"):
