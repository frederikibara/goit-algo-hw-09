from utils.adress_book_manager import AddressBook
from parsing.parser import parse_input
from utils.serialize import *
from handlers.handler import *
from adapters.console import ConsoleAdapter


def main():
    """
Main contains the basic functionality of the bot assistant application.
It handles user interactions such as adding, modifying and displaying contacts.

Update:
   - added interface : IUserInterface
   - added adapter : ConsoleAdapter implements IUserInterface
   - fixed method for clear all contacacts from file
   - program structure extends

Commands:
    - hello : Just a greeting.
    - add <name> <phone> : Adds a new contact.
    - mod <name> <new_phone>: Updates an existing contact.
    - del <name> Deletes an existing contact.
    - phone <name>: Displays the contact's phone number.
    - all: Displays all contacts.
    - clear: Deletes all contacts.  
    - add-b <name> <DD.MM.YYYY> : Adds a birthday date
    - show-b <name> : Shows a birthday date
    - b-days : displays a list of birthdays for the next 7 days
    - exit or close: Exits the program.
  """
    
    DATA = 'book.pkl'
    book = load_from_file(DATA)
    print(book)
    
    console = ConsoleAdapter()
    console.show_welcome()   

    while True:
        user_input = input('Enter a command: ')
        command, *args = parse_input(user_input)

        match command:
            case 'hello': 
                console.show_message('How can I help you?')
            case 'add': 
                console.show_message(add_contact(args, book))
            case 'mod': 
                console.show_message(modify_contact(args, book))
            case 'del':
                console.show_message(delete_contact(args, book))
            case 'phone':
                console.show_message(show_phone(args, book))            
            case 'all':
                console.show_contact_list(show_all(book))           
            case 'clear':
                console.show_message(clear_all_data(DATA))
            case 'add-b':
                console.show_message(add_birthday(args, book))
            case 'show-b':
                console.show_message(show_birthday(args, book))
            case 'b-days':
                console.show_message(birthdays(args, book))                      
            case 'exit' | 'close':
                save_to_file(book, DATA)
                console.show_message('Good bye!\n')
                break
            case _ :
                console.show_error('Invalid command')


if __name__ == '__main__':
    main()
