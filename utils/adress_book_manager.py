from collections import UserDict
from utils.emoji_bank import get_emoji
from datetime import datetime, date, timedelta


class AddressBook(UserDict):
    def __init__(self):
        super().__init__()

    def add_record(self, record):
        self.data[record.name.value] = record
        return f'Complete : \'{record.name.value}\' has been added to book'

    def delete_record(self, name):
        if name in self.data:
            del self.data[name]
            return f'Complete : \'{name}\' has been removed'
        return 'Contact not found'

    def find(self, name):
        return self.data.get(name, None)

    def get_upcoming_birthdays(self):
        today = date.today()
        upcoming_birthdays = []

        for record in self.data.values():
            if record.birthday:
                birthday_date = record.birthday.value
                days_until_birthday = (birthday_date - today).days
                if 0 <= days_until_birthday <= 7:
                    upcoming_birthdays.append({
                        'name': record.name.value,
                        'birthday': birthday_date.strftime('%d.%m.%Y')
                    })

        for birthday in upcoming_birthdays:
            b_date = datetime.strptime(birthday['birthday'], '%d.%m.%Y').date()
            if b_date.weekday() in (5, 6):
                b_date += timedelta(days=(7 - b_date.weekday()))
                birthday['birthday'] = b_date.strftime('%d.%m.%Y')
        return upcoming_birthdays

    def __str__(self):
        if not self.data:
            return f'{get_emoji(7)}{get_emoji(1)} Address book is empty{get_emoji(8)}'

        items = []
        for key, record in self.data.items():
            items.append(f'{get_emoji(6)} {record.name.value} : {', '.join(p.value for p in record.phones)}')
        # return "\n".join(items)
        return f'{get_emoji(7)}{"\n".join(items)}{get_emoji(8)}'
