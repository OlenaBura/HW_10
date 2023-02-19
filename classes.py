from collections import UserDict


class Field:
    def __init__(self, value):
        self.value = value


class Name(Field):
    pass


class Phone(Field):
    pass


class Record:
    def __init__(self, name, phone):
        self.name = name
        self.phones = []
        if phone:
            self.phones.append(phone)

    def add_phones(self, phone):
        if phone not in self.phones:
            self.phones.append(phone)

    def change_phones(self, phone, phone_new):
        for count, ele in enumerate(self.phones):
            if ele == phone:
                self.phones[count] = phone_new
                break

    def remove_phones(self, phone):
        for count, element in enumerate(self.phones):
            if element == phone:
                self.phones.remove(element)
                break

    def list_phones(self):
        return self.phones


class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record
        return self.data


name1 = Name('Helen')
print(name1.value)
name2 = Name('Poly')
phone1 = Phone('0970000000')
print(phone1.value)
phone2 = Phone('0960000000')
phone3 = Phone('0980000000')
phone4 = Phone('0500000000')
record1 = Record(name1, phone1.value)
record2 = Record(name2, phone2.value)
print(record1.name.value)
record1.add_phones(phone2.value)
record1.add_phones(phone3.value)
print(record1.list_phones())
record1.change_phones(phone1.value, phone4.value)
print(record1.list_phones())
record1.remove_phones(phone4.value)
print(record1.list_phones())
book1 = AddressBook()
print(book1.add_record(record1))
print(book1.add_record(record2))