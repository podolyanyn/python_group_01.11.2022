from datetime import date


class Phonebook:

    def __init__(self):
        self.users_accounts = []
        self.date = date.today()
        self.indexes = list(range(100001, 999999))

    def __repr__(self):
        return f"There are {len(self.users_accounts)} users in the phonebook. The phonebook was created on {self.date}"

    def __str__(self):
        return f"Number: {len(self.users_accounts)}.\nDate: {self.date}"

    def new_user(self, first_name, last_name, phone_number, location):
        user = User(first_name, last_name, phone_number, location, self.indexes[0])
        self.indexes.pop(0)
        self.users_accounts.append(user)
        return user

    def change_name(self, identification, full_name):
        for user in self.users_accounts:
            if user.unique_id == identification:
                user.first_name, user.last_name = full_name.split()

    def change_number(self, identification, number):
        for user in self.users_accounts:
            if user.unique_id == identification:
                user.phone_number = number

    def change_location(self, identification, location):
        for user in self.users_accounts:
            if user.unique_id == identification:
                user.location = location

    def upload_data(self):
        with open("phonebookClass.json", "w") as phone_book:
            for user in self.users_accounts:
                phone_book.write(f"Name: {user.full_name},\nPhone: {user.phone_number},\nLocation: {user.location},\nID: {user.unique_id}\n\n")


class User:

    def __init__(self, first_name, last_name, phone_number, location, unique_id):
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number
        self.location = location
        self.unique_id = unique_id

    def __str__(self):
        return f"{self.full_name}, {self.phone_number}, {self.location}, {self.unique_id}"

    @property
    def full_name(self):
        full_name = f"{self.first_name} {self.last_name}"
        return full_name

    def change_name(self, full_name):
        self.first_name, self.last_name = full_name.split()

    def change_number(self, number):
        self.phone_number = number

    def change_location(self, location):
        self.location = location


phonebook = Phonebook()

phonebook.new_user("Valery", "Rudobelets", "+380955048230", "Dnipro")
phonebook.new_user("Jiri", "Krutsky", "+392234934923", "Prague")
phonebook.new_user("Bartosz", "Grzyb", "+563453534543", "Warsaw")
phonebook.new_user("Lee", "San", "+123453546453", "Toronto")
phonebook.new_user("Asuka", "Langley", "+233242432233", "Osaka")

phonebook.change_name(100001, "Valerie Rudobelec")

phonebook.upload_data()
print(phonebook.users_accounts[0])
