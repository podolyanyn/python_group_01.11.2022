# # task_1
#
class Animal:

    def __init__(self, name):
        self.name = name

    def talk(self):
        raise NotImplementedError("Must be implemented by a subclass")


class Dog(Animal):

    def talk(self):
        return "Whoof"


class Cat(Animal):

    def talk(self):
        return "Meow"


class Cow(Animal):

    def talk(self):
        return "Moo"


class Bird(Animal):

    def talk(self):
        return "Tweet"


class ArussianWarship(Animal):

    def talk(self):
        return "F*** itself"

animals = [Cat("Maja"), Dog("Spike"), Cow("Big Tasty"), Bird("Ostrich"), ArussianWarship("Ivan")]


def child_game(lst):
    correct_answer = 0
    wrong_answer = 0
    while correct_answer != len(lst):
        for item in lst:
            user_input = input(f"{item.name} goes...")
            if user_input != item.talk():
                wrong_answer += 1
                print("That's a wrong answer. Try better next time")
            elif user_input == item.talk():
                correct_answer += 1
                print("Hooray! That's a correct one!")
        return f"That's the end of the game. Correct answers are {correct_answer} and wrong numbers are {wrong_answer}"
#
#
# # print(child_game(animals))
#
#
# # task_2
# Я вирішив, але мені не дуже подобається як реалізоване додавання книг конкретного автора до екземпляру класу автора
# я хотів аби воно додавалося одразу в методі new_book, але чомусь працює лише через наступний метод і я не дуже
# розумію чому

class Library:

    def __init__(self, name, books=[], authors=[]):
        self.name = name
        self.books = books
        self.authors = authors

    def __repr__(self):
        return f"{self.name}: \nAuthors: {self.authors} \nBooks: {self.books}"

    def __str__(self):
        return f"{self.name}: \nAuthors: {self.authors} \nBooks: {self.books}"

    def new_book(self, name, year, author):
        book = Book(name, year, author)
        self.books.append(book)
        if author not in self.authors:
            self.authors.append(author)
        return book

    def remove_book(self, book):
        self.books.remove(book)

    def group_by_author(self, author):
        lst = [book for book in self.books if book.author == author]
        author.books = lst
        return lst

    def group_by_year(self, year: int):
        return [book for book in self.books if book.year == year]


class Book:
    number_of_books = 0

    def __init__(self, name, year, author):
        self.name = name
        self.year = year
        self.author = author

        Book.number_of_books += 1

    def __repr__(self):
        return f"\n<{self.__class__.__name__} Title = {self.name},\nYear = {self.year}>"

    def __str__(self):
        return f"\n<{self.__class__.__name__} Title = {self.name},\nYear = {self.year}>"


class Author:

    def __init__(self, name, country, birthday, books=[]):
        self.name = name
        self.country = country
        self.birthday = birthday
        self.books = books

    def __repr__(self):
        return f"<\n{self.__class__.__name__}\n{self.name}: \ncountry = {self.country}, \ndate of birth = {self.birthday}, \n{self.books}>"

    def __str__(self):
        return f"<\n{self.__class__.__name__} \n{self.name}: \ncountry = {self.country}, \ndate of birth = {self.birthday}, \n{self.books}>"


library = Library("Central Library")
author1 = Author("J.K.Rowling", "The United Kingdom", "31.06.1965")
author2 = Author("Serhij Žadan", "Ukraine", "23.08.1974")
author3 = Author("Taras Ševčenko", "Ukraine", "09.03.1814")
author4 = Author("Terry Pratchett", "The United Kingdom", "24.04.1948")
author5 = Author("Stanislaw Lem", "Poland", "12.09.1921")
library.new_book("Philosopher's Stone", 1997, author1)
library.new_book("Internat", 2017, author2)
library.new_book("Depesh Mode", 2004, author2)
library.new_book("Kobzar", 1840, author3)
library.new_book("Colour of Magic", 1983, author4)
library.new_book("Cyberiada", 1978, author5)
library.new_book("Solaris", 1976, author5)
library.new_book("Chamber of Secrets", 1998, author1)
library.new_book("Prisoner of Azkaban", 1999, author1)
library.new_book("Goblet of Fire", 2000, author1)
library.new_book("Order of the Phoenix", 2003, author1)
library.new_book("Half-Blood Prince", 2005, author1)
library.new_book("Deathly Hallows", 2007, author1)
library.group_by_author(author1)
library.group_by_author(author2)
library.group_by_author(author3)
library.group_by_author(author4)
library.group_by_author(author5)
# print(author1)
print(library.books[0])
library.remove_book(library.books[0])
print(library.books[0])

# task_3


class Fraction:

    def __init__(self, x, y=1):
        self.truediv = x / y

    def __add__(self, other):
        return Fraction(self.truediv+other.truediv)

    def __mul__(self, other):
        return Fraction(self.truediv*other.truediv)

    def __truediv__(self, other):
        return Fraction(self.truediv/other.truediv)

    def __sub__(self, other):
        return Fraction(self.truediv-other.truediv)

    def __eq__(self, other):
        if isinstance(other, Fraction):
            return self.truediv == other.truediv
        return False

    def __repr__(self):
        return f"<Fraction: {self.truediv}>"



if __name__ == "__main__":
    x = Fraction(1, 2)
    y = Fraction(1, 4)
    # print(x + y == Fraction(3, 4))

