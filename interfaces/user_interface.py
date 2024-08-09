from abc import ABC, abstractmethod

class IUserInterface:
    
    @abstractmethod
    def show_message(self, msg: str) -> None:
        pass
    @abstractmethod
    def show_contact_list(self, contacts) -> None:
        pass
    @abstractmethod
    def show_error(self, error: str) -> None:
        pass
    @abstractmethod
    def show_welcome(self) -> None:
        pass