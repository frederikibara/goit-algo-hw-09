from utils.emoji_bank import get_emoji
from functools import wraps
from utils.adress_book_manager import AddressBook
from models.models import *


def input_error(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError as e:
            return f'Error: {str(e)}'
        except KeyError:
            return 'Error: Key not found'
        except IndexError:
            return 'Error: Index out of range'
        except Exception as e:
            return f'An unexpected error occurred: {str(e)}'
    return wrapper


@input_error
def add_contact(args, book: AddressBook):
    """
    Adding/Updating contact name or phone number
    """
    
    name, phone, *_ = args
    record = book.find(name)
    
    if record is None:
        record = Record(name)
        book.add_record(record)
        message = 'Contact added.'
    else:
        message = 'Contact updated.'
    
    if phone:
        try:
            return record.add_phone(phone) + f'{get_emoji(0)}  {message}'
        except ValueError as e:
            return str(e)
    
    return message    


@input_error
def modify_contact(args, book: AddressBook):
    """
    Modify phone number for an existing contact
    """
    if len(args) < 3:
        return 'Error: Not arguments for modify command'
    
    name, old_phone, new_phone = args
    record = book.find(name)
    if record:
        try:
            return record.edit_phone(old_phone, new_phone)
        except ValueError as e:
            return str(e)
    else:
        return 'Contact not found'


@input_error
def show_phone(args, book: AddressBook):
    """
    Show phone numbers for a contact
    """
    if len(args) < 1:
        return 'Error: Not enough arguments provided for phone command'

    name = args[0]
    record = book.find(name)
    if record:
        if record.phones:
            return f'Phones {get_emoji(4)}   {name}: {', '.join(p.value for p in record.phones)}'
        else:
            return f'No phones found for {name}'
    else:
        return 'Contact not found'


@input_error
def show_all(book: AddressBook):
    """
    Show all contacts in the address book
    """
    return str(book)


@input_error
def delete_contact(args, book: AddressBook):
    """
    Delete a contact by name
    """
    if len(args) < 1:
        return 'Error: Not arguments for delete command'

    name = args[0]
    return f' {book.delete_record(name)} {get_emoji(2)}'


@input_error
def clear_all_contacts(book: AddressBook):
    """
    Clear all contacts from the address book
    """
    return book.clear()


@input_error
def add_birthday(args, book: AddressBook):
    """
    Add birthday to a contact
    """
    name, date, *_ = args
    record = book.find(name)
    if record:
        return record.add_birthday(date)
    else:
        return 'Contact not found'


@input_error
def show_birthday(args, book: AddressBook):
    """
    Show birthday of a contact
    """
    name, *_ = args
    record = book.find(name)
    if record and record.birthday:
        return f'{record.name.value}\'s birthday {get_emoji(3)}  {record.birthday.value}'
    elif record:
        return 'No birthday set for this contact'
    else:
        return 'Contact not found'


@input_error
def birthdays(args, book: AddressBook):
    """
    Show upcoming birthdays within the next week
    """
    upcoming_birthdays = book.get_upcoming_birthdays()
    if not upcoming_birthdays:
        return 'No upcoming birthdays in the next 7 days'
    
    result = []
    for birthday in upcoming_birthdays:
        result.append(f"{birthday['name']} {get_emoji(3)} {birthday['birthday']}")
        
    return '\n'.join(result)
