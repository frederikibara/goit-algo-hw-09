from datetime import datetime, date, timedelta


class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


class Name(Field):
    def __init__(self, value):
        if not value or value.isspace():
            raise ValueError('Name is empty')
        if any(char.isdigit() for char in value):
            raise TypeError('Name should not contain digits')
        super().__init__(value.title())


class Phone(Field):
    operators_code = ('063', '073', '093', '091', '044',
                      '050', '066', '095', '099', '039',
                      '067', '068', '096', '097', '098')

    def __init__(self, value):
        __max_num_length = 10
        if not value.isdigit() or len(value) > __max_num_length:
            raise ValueError('Invalid phone number')
        if value[:3] not in self.operators_code:
            raise ValueError('Unknown operator')
        super().__init__(value)


class Birthday(Field):
    def __init__(self, value):
        try:
            self.value = datetime.strptime(value, '%d.%m.%Y').date()
        except ValueError:
            raise ValueError('Invalid date format. Use DD.MM.YYYY')


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
        self.birthday = None

    def add_phone(self, phone):
        if phone not in [p.value for p in self.phones]:
            phone_obj = Phone(phone)
            self.phones.append(phone_obj)
            return f'Complete : \'{phone}\' '
        else:
            raise ValueError('This phone is already in the phones list')

    def remove_phone(self, phone):
        phone_obj = self.find_phone(phone)
        if phone_obj:
            self.phones.remove(phone_obj)
            return f'Complete : \'{phone}\' '
        else:
            raise ValueError('This phone is not in the list')

    def edit_phone(self, phone, new_phone):
        phone_obj = self.find_phone(phone)
        if phone_obj:
            self.remove_phone(phone)
            self.add_phone(new_phone)
            return f'Complete : \'{phone}\' has been changed to \'{new_phone}\''
        else:
            raise ValueError('This phone is not in the list')

    def find_phone(self, p) -> Phone:
        for phone in self.phones:
            if phone.value == p:
                return phone
        return None

    def add_birthday(self, date):
        self.birthday = Birthday(date)
        return f'Birthday for {self.name.value} set to {self.birthday.value}'

    def __str__(self):
        birthday_str = f', birthday: {self.birthday.value}' if self.birthday else ''
        return f'Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}{birthday_str}'
