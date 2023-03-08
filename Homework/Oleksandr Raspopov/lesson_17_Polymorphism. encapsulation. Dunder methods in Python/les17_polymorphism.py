print('- - - - Task 1 - Method overloading - - - -\n')


# Create a base class named Animal with a method called talk and then create two subclasses: Dog and Cat,
# and make their own implementation of the method talk be different.
# For instance, Dog’s can be to print ‘woof woof’, while Cat’s can be to print ‘meow’.
# Also, create a simple generic function, which takes as input instance of a Cat or Dog classes
# and performs talk method on input parameter.


class Animal:
    def talk(self):
        pass


class Cat(Animal):
    def talk(self):
        print('meow')


class Dog(Animal):
    def talk(self):
        print('woof woof')


def sound(animal):
    animal.talk()


dog1 = Dog()
cat1 = Cat()
dog1.talk()
cat1.talk()

sound(dog1)
sound(cat1)

print('\n- - - - Task 2 - Library - - - -\n')


# Write a class structure that implements a library. Classes:
# 1) Library - name, books = [], authors = []
# 2) Book - name, year, author (author must be an instance of Author class)
# 3) Author - name, country, birthday, books = []
# Library class
# Methods:
# - new_book(name: str, year: int, author: Author) - returns an instance of Book class
# and adds the book to the books list for the current library.
# - group_by_author(author: Author) - returns a list of all books grouped by the specified author
# - group_by_year(year: int) - returns a list of all the books grouped by the specified year
# All 3 classes must have a readable __repr__ and __str__ methods.
# Also, the book class should have a class variable which holds the amount of all existing books


class Library:
    def __init__(self, name):
        self.name = name
        self.books = []
        self.author = []

    def new_book(self, name: str, year: int, author):
        new_book = Book(name, year, author)
        self.books.append(new_book)
        self.author.append(author)
        Book.books += 1
        author.books.append(new_book)
        return new_book

    def group_by_author(self, author):
        books_list = []
        for book in self.books:
            if book.author == author:
                books_list.append(book)
        return books_list

    def group_by_year(self, year: int):
        books_list = []
        for book in self.books:
            if book.year == year:
                books_list.append(book)
        return books_list

    def __repr__(self):
        return f'Name: {self.name}\n' \
               f'books:{self.books}\n' \
               f'author: {self.author}'


class Book:
    books = 0

    def __init__(self, name, year, author):
        self.name = name
        self.year = year
        self.author = author

    def __repr__(self):
        return f'name: {self.name}'


class Author:
    def __init__(self, name, country, birthday):
        self.name = name
        self.country = country
        self.birthday = birthday
        self.books = []

    def __repr__(self):
        return f'Name: {self.name}'


auth1 = Author('Mykola', 'Ukraine', '1930')
auth2 = Author('Petro', 'Ukraine', '1950')
book1 = Book('Abetka', '1960', auth1)
book2 = Book('Book', '1980', auth2)
lib1 = Library('Main')
print(lib1)
print()
lib1.new_book('Abetka+', 1960, auth1)
lib1.new_book('Book+', 1980, auth2)
print(lib1)
print()

print(lib1.group_by_author(auth1))
print(lib1.group_by_year(1980))

print('\n- - - - Task 3 - Fraction - - - -\n')


# Створіть клас Fraction, який буде представляти всю базову арифметичну логіку для дробів (+, -, /, *) з належною
# перевіркою й обробкою помилок. Потрібно додати магічні методи для математичних операцій та операції порівняння між
# об'єктами класу Fraction


class Fraction:
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        if denominator == 0:
            raise ZeroDivisionError('Denominator must be else then NULL')
        else:
            self.denominator = denominator

    def __gcd(self, other):
        from math import gcd
        common = gcd(self.numerator, other)
        numerator = int(self.numerator / common)
        denominator = int(other / common)
        return Fraction(numerator, denominator)

    def __add__(self, other):
        numerator1 = self.numerator * other.denominator
        numerator2 = other.numerator * self.denominator
        denominator = self.denominator * other.denominator
        numerator = numerator1 + numerator2
        return Fraction.__gcd(numerator, denominator)

    def __sub__(self, other):
        numerator1 = self.numerator * other.denominator
        numerator2 = other.numerator * self.denominator
        denominator = self.denominator * other.denominator
        numerator = numerator1 - numerator2
        return Fraction.__gcd(numerator, denominator)

    def __mul__(self, other):
        numerator = self.numerator * other.numerator
        denominator = self.denominator * other.denominator
        return Fraction.__gcd(numerator, denominator)

    def __truediv__(self, other):
        if other.numerator == 0:
            raise ZeroDivisionError('Denominator must be else then NULL')
        else:
            numerator = self.numerator * other.denominator
            denominator = self.denominator * other.numerator
            return Fraction.__gcd(numerator, denominator)

    def __str__(self):
        return f'Fraction({self.numerator}, {self.denominator})'


if __name__ == "__main__":
    x = Fraction(1, 2)
    y = Fraction(1, 4)
    print(f'{x} + {y} = {x + y}')
    print(f'{x} - {y} = {x - y}')
    print(f'{x} * {y} = {x * y}')
    print(f'{x} / {y} = {x / y}')

    print(x + y == Fraction(3, 4))  # why not True ?
    print(id(Fraction(3, 4)) == id(x + y))
    print(isinstance(Fraction(3, 4), type(x + y)))
    print()

    x = Fraction(20, 2)
    y = Fraction(40, 2)
    print(f'{x} + {y} = {x + y}')
    print(f'{x} - {y} = {x - y}')
    print(f'{x} * {y} = {x * y}')
    print(f'{x} / {y} = {x / y}')

    # x = Fraction(1, 0)
