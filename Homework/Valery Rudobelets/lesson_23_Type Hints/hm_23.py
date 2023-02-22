from datetime import date

# task_1 = тут наче як не так багато змінних які можна позначити, більше інпутів, де наче й так буде str
import json


def phonebook():
    user_input = input("Hello, I am your phonebook creator.\n"
                       "To create a phonebook, press C.\n"
                       "If you want to update the book, press U.\n"
                       "If you need to delete a profile, press D.\n"
                       "If you would like to find a profile, press S.\n"
                       "Press Q to quit.")
    phone_lst: list = []
    while user_input != "Q":
        match user_input:
            case "C":
                phone_dic: dict = {}
                name = input("Please, enter your firstname: ")
                surname = input("Please, enter your last name: ")
                phone_number = input("Please, enter your phone number: ")
                location = input("Please, enter your location in the following format - City, Country: ")
                stop = input("In case you want to stop filling in the book, type Q. Else - type any button.")
                phone_dic["Name"] = name
                phone_dic["Surname"] = surname
                phone_dic["Number"] = phone_number
                phone_dic["Location"] = location
                phone_lst.append(phone_dic)
                if stop == "Q":
                    with open("phonebook.json", "w") as phone_book:
                        return json.dump(phone_lst, phone_book, indent=2)
            case "U":
                with open("phonebook.json") as phone_book:
                    data = json.load(phone_book)
                question = input("What would you like to change? Name, Surname, Number or Location? Press Q to quit: ")
                if question == "Name":
                    question_next = input(f"Whose {question} would you like to change?: ")
                    # mistake_prove_question = mpq
                    mpq_1 = input("Just to be sure - what's their phone number?: ")
                    new_name = input(f"Type a new {question} here: ")
                    for item in data:
                        if item["Name"] == question_next and item["Number"] == mpq_1:
                            item["Name"] = new_name
                            with open("phonebook.json", "w") as phone_book:
                                return json.dump(data, phone_book, indent=2)
                        else:
                            print("There's no such data, try again.")
                            return phonebook()
                elif question == "Surname":
                    question_next = input(f"Whose {question} would you like to change?: ")
                    # mistake_prove_question = mpq
                    mpq_1 = input("Just to be sure - what's their phone number?: ")
                    new_name = input(f"Type a new {question} here: ")
                    for item in data:
                        if item["Surname"] == question_next and item["Number"] == mpq_1:
                            item["Surname"] = new_name
                            with open("phonebook.json", "w") as phone_book:
                                return json.dump(data, phone_book, indent=2)
                        else:
                            print("There's no such data, try again.")
                            return phonebook()
                elif question == "Location":
                    question_next = input(f"Whose {question} would you like to change?: ")
                    # mistake_prove_question = mpq
                    mpq_1 = input("Just to be sure - what's their phone number?: ")
                    new_name = input(f"Type a new {question} here: ")
                    for item in data:
                        if item["Location"] == question_next and item["Number"] == mpq_1:
                            item["Location"] = new_name
                            with open("phonebook.json", "w") as phone_book:
                                return json.dump(data, phone_book, indent=2)
                        else:
                            print("There's no such data, try again.")
                            return phonebook()
                elif question == "Number":
                    question_next = input(f"Whose {question} would you like to change?: ")
                    # mistake_prove_question = mpq
                    mpq_1 = input("Just to be sure - what's their name?: ")
                    mpq_2 = input("And one more question - what's their surname?: ")
                    new_name = input(f"Type a new {question} here: ")
                    for item in data:
                        if item["Number"] == question_next and item["Name"] == mpq_1 and item["Surname"] == mpq_2:
                            item["Number"] = new_name
                            with open("phonebook.json", "w") as phone_book:
                                return json.dump(data, phone_book, indent=2)
                        else:
                            print("There's no such data, try again.")
                            return phonebook()
                elif question == "Q":
                    with open("phonebook.json", "w") as phone_book:
                        return json.dump(data, phone_book, indent=2)
            case "D":
                with open("phonebook.json") as phone_book:
                    data = json.load(phone_book)
                choice = input("Type the number of the person whose profile you would like to delete: ")
                for item in data:
                    if item["Number"] == choice:
                        data.remove(item)
                    elif choice == "Q":
                        with open("phonebook.json", "w") as phone_book:
                            return json.dump(phone_lst, phone_book)
                    with open("phonebook.json", "w") as phone_book:
                        return json.dump(data, phone_book, indent=2)
            case "S":
                with open("phonebook.json") as phone_book:
                    data = json.load(phone_book)
                question = input("Enter the parameter by which you'd like to find a profile - "
                                 "Name, Surname, Number, Location or Full name: ")
                if question == "Name":
                    question_next = input(f"Okay, what's the {question}?")
                    for item in data:
                        if item["Name"] == question_next:
                            return item
                elif question == "Surname":
                    question_next = input(f"Okay, what's the {question}?")
                    for item in data:
                        if item["Surname"] == question_next:
                            return item
                elif question == "Number":
                    question_next = input(f"Okay, what's the {question}?")
                    for item in data:
                        if item["Number"] == question_next:
                            return item
                elif question == "Location":
                    question_next = input(f"Okay, what's the {question}?")
                    for item in data:
                        if item["Location"] == question_next:
                            return item
                elif question == "Full name":
                    question_next = input(f"Okay, what's the {question}?")
                    for item in data:
                        full_name = question_next.split()
                        if item["Name"] == full_name[0] and item ["Surname"] == full_name[1]:
                            return item
            case "Q":
                with open("phonebook.json", "w") as phone_book:
                    return json.dump(phone_lst, phone_book)

# task_1.2 тут наче краще це зобразити можна


class Phonebook:

    def __init__(self):
        self.users_accounts: list = []
        self.date = date.today()
        self.indexes: list = list(range(100001, 999999))

    def __repr__(self):
        return f"There are {len(self.users_accounts)} users in the phonebook. The phonebook was created on {self.date}"

    def __str__(self):
        return f"Number: {len(self.users_accounts)}.\nDate: {self.date}"

    def new_user(self, first_name: str, last_name: str, phone_number: str, location: str):
        user: User = User(first_name, last_name, phone_number, location, self.indexes[0])
        self.indexes.pop(0)
        self.users_accounts.append(user)
        return user

    def change_name(self, identification: int, full_name: str):
        for user in self.users_accounts:
            if user.unique_id == identification:
                user.first_name, user.last_name = full_name.split()

    def change_number(self, identification: int, number: str):
        for user in self.users_accounts:
            if user.unique_id == identification:
                user.phone_number = number

    def change_location(self, identification: int, location: str):
        for user in self.users_accounts:
            if user.unique_id == identification:
                user.location = location

    def upload_data(self):
        with open("phonebookClass.json", "w") as phone_book:
            for user in self.users_accounts:
                phone_book.write(f"Name: {user.full_name},\nPhone: {user.phone_number},\nLocation: {user.location},\nID: {user.unique_id}\n\n")


class User:

    def __init__(self, first_name: str, last_name: str, phone_number: str, location: str, unique_id: int):
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number
        self.location = location
        self.unique_id = unique_id

    def __str__(self):
        return f"{self.full_name}, {self.phone_number}, {self.location}, {self.unique_id}"

    @property
    def full_name(self):
        full_name: str = f"{self.first_name} {self.last_name}"
        return full_name

    def change_name(self, full_name):
        self.first_name, self.last_name = full_name.split()

    def change_number(self, number: str):
        self.phone_number = number

    def change_location(self, location: str):
        self.location = location














