import pickle
from utils.adress_book_manager import AddressBook


def save_to_file(book, file):
    with open(file, 'wb') as wr:
        pickle.dump(book, wr)


def load_from_file(file):
    try:
        with open(file, 'rb') as rd:
            return pickle.load(rd)
    except FileNotFoundError:
        return AddressBook()
    except EOFError:
        return AddressBook()
        
            