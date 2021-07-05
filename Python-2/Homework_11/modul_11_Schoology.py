from collections import UserDict
import datetime
import re


class Field:
    def __init__(self, value):
        self.__value = value

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, new_value):
        self.__value = new_value


class Name(Field):

    def __init__(self, value):
        self.value = value


pattern_for_phone = '\d{3,}'


class Phone(Field):

    def __init__(self, value):
        self.value = value

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, new_value):
        if re.fullmatch(pattern_for_phone, new_value):
            self.__value = new_value
        else:
            print('Wrong phone number')
            self.__value = None


class Birthday(Field):

    def __init__(self, value):
        self.value = value

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, new_value):
        numbers_date = re.split(r'[\.,\- /:]+', new_value)
        numbers_date = tuple(map(int, numbers_date))
        try:
            date_birthday = datetime.datetime(*numbers_date).date()

            if date_birthday >= datetime.datetime.today().date():
                print('Date from future')
                self.__value = None
                return
            self.__value = date_birthday
        except:
            print('Date is wrong')
            self.__value = None


class AddressBook(UserDict):

    def add_record(self, record):
        self[record.name.value] = record

    def iterator(self, N):
        self.N = N
        self.i = 0
        new_iter = self
        while self.i < len(self.data): 
            yield ''.join(str(list(next(new_iter).items())))

    def __next__(self):
        if self.i >= len(self):
            raise StopIteration
        lst_items = list(self.data.items())
        cuter_items = dict(lst_items[self.i: self.i + self.N])
        self.i += self.N
        return cuter_items

    def __iter__(self, N=1):
        self.i = 0
        return self


class Record():

    def __init__(self, name, phone=[], birthday=None):
        self.name = name
        self.phones = [phone]
        self.birthday = birthday

    def add_phone(self, phone):
        self.phones.append(phone)

    def change_phone(self, phone):
        pass

    def days_to_birthday(self):
        now = datetime.datetime.today().date()
        bd = self.birthday.value
        bd_that_year = bd.replace(year=now.year)
        delta_bd = bd_that_year - now
        if delta_bd.days <= 0:
            bd_that_year = bd_that_year.replace(year=now.year+1)
            delta_bd = bd_that_year - now

        if (self.birthday.value.day, self.birthday.value.month) == (29, 2):
            return delta_bd.days - 1
        return delta_bd.days