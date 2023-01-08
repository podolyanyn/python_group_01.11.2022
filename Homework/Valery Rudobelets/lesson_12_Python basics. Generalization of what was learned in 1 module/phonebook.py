#task_2
import json


def phonebook():
    user_input = input("Hello, I am your phonebook creator.\n"
                       "To create a phonebook, press C.\n"
                       "If you want to update the book, press U.\n"
                       "If you need to delete a profile, press D.\n"
                       "If you would like to find a profile, press S.\n"
                       "Press Q to quit.")
    phone_lst = []
    while user_input != "Q":
        match user_input:
            case "C":
                phone_dic = {}
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


# print(phonebook())

print(type(phonebook))












