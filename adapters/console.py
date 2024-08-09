from interfaces.user_interface import IUserInterface

class ConsoleAdapter(IUserInterface):
    
    def show_message(self, msg):
        print(msg)    
    
    def show_contact_list(self, contacts):
        if not contacts:
            self.show_message('Contacts is empty')         
        self.show_message(contacts)
    
    
    def show_error(self, error):
        print(f'Error : {error}')
    
    
    def show_welcome(self):
        self.show_message('WELCOME to the ASSISTANT BOT!')