from address_book import AddressBook
import os
import pickle
    
DATA_FOLDER = "data"
FILENAME = "addressbook.pkl"
FILEPATH = os.path.join(DATA_FOLDER, FILENAME)

def save_data(book, filepath=FILEPATH):
    if not os.path.exists(DATA_FOLDER):
        os.makedirs(DATA_FOLDER)
    with open(filepath, "wb") as f:
        pickle.dump(book, f)

def load_data(filepath=FILEPATH):
    try:
        with open(filepath, "rb") as f:
            return pickle.load(f)
    except FileNotFoundError:
        return AddressBook() 