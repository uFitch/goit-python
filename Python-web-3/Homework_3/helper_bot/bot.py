from datetime import datetime, timedelta
import pickle
import re
import os

UI = '''
1. Add new contact
2. View contacts
3. Search contact
4. Update contact
5. Delete contact
6. Reset all
7. Show birthday list
8. Exit
'''

validate_msg = ''' 
Wrong data, please use next:
1. Only letters for name
2. Only digits for phone(lenght must be equal 10)
3. Letters, digits, other symbols and @ for mail
4. For birthday use next pattern: dd.mm.yyyy
'''

contact_head = "|{:<15}|{:<15}|{:<15}|{:<24}|{:<15}|{:<15}".format('Name', 'Address', 'Phone', 'E-mail', 'Birthday', 'Note')

class User(object):

    def __init__(self, name=None, address=None, phone=None, mail=None, birthday=None, note=None):
        self.name = name
        self.address = address
        self.phone = phone
        self.mail = mail
        self.birthday = birthday
        self.note = note

    def __iter__(self):
        return self

    def __next__(self):
        try:
            item = self.birthday
        except AttributeError:
            raise StopIteration
        return item

    def __str__(self):
        return "|{:<15}|{:<15}|{:<15}|{:<24}|{:<15}|{:<15}".format(self.name, self.address, self.phone, self.mail, self.birthday, self.note)


class Application(object):

    def __init__(self, database):
        self.database = database
        self.persons = {}
        if not os.path.exists(self.database):
            file_pointer = open(self.database, 'wb')
            pickle.dump({}, file_pointer)
            file_pointer.close()
        else:
            with open(self.database, 'rb') as person_list:
                self.persons = pickle.load(person_list)

    def add(self):
        try:
            name, address, phone, mail, birthday, note = self.getdetails()
            if name not in self.persons:
                self.persons[name] = User(name, address, phone, mail, birthday, note)
                print("Contact was added")
            else:
                print("Contact already present.")
        except:
            print("Contact not added! Please try again!")
    
    def viewall(self):
        if self.persons:
            print(contact_head)
            for person in self.persons.values():
                print(person)
        else:
            print("No contacts in database.")
    
    def search(self):
        name = input("Enter the name: ")
        if name in self.persons:
            print(contact_head)
            print(self.persons[name])
        else:
            print("Contact not found.")

    def update(self):
        name = input("Enter the name: ")
        try:
            if name in self.persons:
                print("Found. Enter new details.")
                name, address, phone, mail, birthday, note = self.getdetails()
                self.persons[name].__init__(name, address, phone, mail, birthday, note)
                print("Successfully updated.")
            else:
                print("Contact not found.")
        except:
            print("You enter wrong data! Please try again!")

    def delete(self):
        name = input("Enter the name to delete: ")
        if name in self.persons:
            del self.persons[name]
            print("Deleted the contact.")
        else:
            print("Contact not found in the app.")

    def getdetails(self):
        name = input("Name: ")
        address = input("Address: ")
        phone = input("Phone:")
        mail = input("Mail: ")
        birthday = input("Birthday: ")
        note = input("Note: ")
        
        if re.findall('[a-zA-Z]+', name) and (re.findall('\d+', phone) and len(phone) == 10) and re.findall('(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)', mail) and re.findall('[0-9]{2}.[0-9]{2}.[0-9]{4}', birthday):
            return name, address, phone, mail, birthday, note
        else:
            print(validate_msg)

    def birthday_list(self):
        days = int(input('enter the number: '))
        tomorrow = datetime.now() + timedelta(days=days)
        tomorrow_formatted = tomorrow.strftime('%d.%m.%Y')
        
        try:
            for names in self.persons.keys():
                if tomorrow_formatted in self.persons[names]:
                    print(names)
        except KeyboardInterrupt:
            print("Manual exit!")

    def reset(self):
        self.persons = {}

    def __del__(self):
        with open(self.database, 'wb') as db:
            pickle.dump(self.persons, db)

    def __str__(self):
        return UI


def main():
    app = Application('contacts.data')
    choice = ''

    while choice != '8':
        print(app)
        choice = input('Choose: ')
        if choice == '1':
            app.add()
        elif choice == '2':
            app.viewall()
        elif choice == '3':
            app.search()
        elif choice == '4':
            app.update()
        elif choice == '5':
            app.delete()
        elif choice == '6':
            app.reset()
        elif choice == '7':
            app.birthday_list()
        elif choice == '8':
            print("Exiting.")
        else:
            print("Invalid choice.")

if __name__ == '__main__':
    main()
