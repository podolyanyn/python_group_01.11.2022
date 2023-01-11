#Task-1
class Animal:
    def talk():
        raise NotImplementedError




class Dog(Animal):
    def talk():
        print('Wof-Wof')



class Cat(Animal):
    def talk():
        print('Meow')


def u_input():
    user_input = input('Enter class: ')
    if user_input == 'Dog':
        Dog.talk()
    elif user_input == 'Cat':
        Cat.talk()



#u_input()


#Task-2
#Запозичив це завдання прошу вибачення за порушення авторських прав
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



#Task-4
def gcd(m,n):
    while m%n != 0:
        oldm = m
        oldn = n

        m = oldn
        n = oldm%oldn
    return n

class Fraction:
    def __init__(self,top,bottom):
         self.num = top
         self.den = bottom

    def __str__(self):
         return str(self.num)+"/"+str(self.den)

    def show(self):
         print(self.num,"/",self.den)

    def __add__(self,otherfraction):
         newnum = self.num*otherfraction.den + \
                      self.den*otherfraction.num
         newden = self.den * otherfraction.den
         common = gcd(newnum,newden)
         return Fraction(newnum//common,newden//common)
    
    def __sub__(self,otherfraciton):
        newnum = self.num*otherfraciton.den - self.den*otherfraciton.den
        newden = self.den * otherfraciton.den

        common = gcd(newnum,newden)

        return Fraction(newnum//common,newden//common)

    def __mul__(self,other):
        newnum = self.num * other.num
        newden = self.den + other.den

        common = gcd(newnum,newden)

        return Fraction(newnum//common,newden//common)    

    def __truediv__(self,other):
        newnum = self.num * other.den
        newden = self.den + other.num

        common = gcd(newnum,newden)

        return Fraction(newnum//common,newden//common)    

        


x = Fraction(1,2)
y = Fraction(2,3)
print(x+y)
print(x == y)