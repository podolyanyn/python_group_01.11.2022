print('--- Task 1 ---\n')  # School
# Make a class structure in python representing people at school.
# Make a base class called Person, a class called Student, and another one called Teacher.
# Try to find as many methods and attributes as you can which belong to different classes,
# and keep in mind which are common and which are not.
# For example, the name should be a Person attribute, while salary should only be available to the teacher.


class Person:
    def __init__(self, name, age, city):
        self.name = name
        self.age = age
        self.city = city

    def birthday(self):
        self.age = self.age + 1

    def __str__(self):
        return f'{self.name}, {self.age}, {self.city}'


class Student(Person):
    def __init__(self, name, age, city, school, course, score):
        super().__init__(name, age, city)
        self.school = school
        self.course = course
        self.score = score

    def course_change(self, new_course):
        self.course = new_course

    def school_leave(self):
        del self.name
        del self.age
        del self.city
        del self.school
        del self.course
        return f'Good luck!'

    def __str__(self):
        return f'{self.name}, {self.age}, {self.city}, {self.school}, {self.course}, {self.score}'


class Teacher(Person):
    def __init__(self, name, age, city, school, subject, degree):
        super().__init__(name, age, city)
        self.school = school
        self.subject = subject
        self.degree = degree

    def ask_student(self, student):
        student.score = 2


student1 = Student('Alexander', 20, 'Dnipro', 'University', 'Math', 5)
teacher1 = Teacher('Igor', 45, 'Kyiv', 'University', 'Math', 'Doctor')
print(student1)  # __str__ of Student(Person)
print(teacher1)  # __str__ of Person, because no __str__ specified for Teacher(Person)
print(f'Score before lesson: {student1.score}')
teacher1.ask_student(student1)
print(f'Score after lesson: {student1.score}')

student1.birthday()  # method of class Person, not Student(Person)
print(student1.age)

# print(dir(student1))
student1.school_leave()
# print(dir(student1))

print('\n--- Task 2 ---\n')  # Mathematician
# Implement a class Mathematician which is a helper class for doing math operations on lists
# The class doesn't take any attributes and only has methods:
# square_nums (takes a list of integers and returns the list of squares)
# remove_positives (takes a list of integers and returns it without positive numbers
# filter_leaps (takes a list of dates (integers) and removes those that are not 'leap years'


class Mathematician:
    def square_nums(self, args):  # takes a list of integers and returns the list of squares
        return [x**2 for x in args]

    def remove_positives(self, args):  # takes a list of integers and returns it without positive numbers
        return [x for x in args if x < 0]

    def filter_leaps(self, args):  # takes a list of dates (integers) and removes those that are not 'leap years'
        return [x for x in args if not x % 4]


m = Mathematician()

print(m.square_nums([7, 11, 5, 4]))
print(m.remove_positives([26, -11, -8, 13, -90]))
print(m.filter_leaps([2001, 1884, 1995, 2003, 2020]))

assert m.square_nums([7, 11, 5, 4]) == [49, 121, 25, 16]
assert m.remove_positives([26, -11, -8, 13, -90]) == [-11, -8, -90]
assert m.filter_leaps([2001, 1884, 1995, 2003, 2020]) == [1884, 2020]


print('\n--- Task 3 ---\n')  # Product Store
# Write a class Product that has three attributes:
# type
# name
# price
# Then create a class ProductStore, which will have some Products and will operate with all products in the store.
# All methods, in case they can’t perform its action, should raise ValueError with appropriate error information.
# Tips: Use aggregation/composition concepts while implementing the ProductStore class.
# You can also implement additional classes to operate on a certain type of product, etc.

# Also, the ProductStore class must have the following methods:
# add(product, amount) - adds a specified quantity of a single product with a predefined price premium for your store(30 percent)
# set_discount(identifier, percent, identifier_type=’name’) - adds a discount for all products specified by input identifiers (type or name).
# The discount must be specified in percentage
# sell_product(product_name, amount) - removes a particular amount of products from the store if available, in other case raises an error.
# It also increments income if the sell_product method succeeds.
# get_income() - returns amount of many earned by ProductStore instance.
# get_all_products() - returns information about all available products in the store.
# get_product_info(product_name) - returns a tuple with product name and amount of items in the store.


class Product:
    def __init__(self, type, name, price):
        self.type = type
        self.name = name
        self.price = price


class ProductStore:

    def __init__(self):
        self.PREMIUM = 1.3
        self.stock = []
        self.pricelist = {}
        self.discounts = {}
        self.sales = []

    def __str__(self):
        return f'stock: {self.stock}\n' \
               f'pricelist: {self.pricelist}\n' \
               f'promo: {self.discounts}'

    def add(self, product, amount):  # adds a specified q-ty of a single product with a predefined price premium (30%)
        price = round(product.price*self.PREMIUM, 2)
        self.stock.append({product.name: amount, 'type': product.type})
        self.pricelist.update({product.name: price})

    def set_discount(self, identifier, percent, identifier_type='name'):  # adds a discount for all products specified by input identifiers (type or name).
        return self.discounts.update({identifier: - percent})

    def sell_product(self, product_name, amount):  # removes a particular amount of products from the store if available, in other case raises an error.
        def checkout(product_name, amount):

            def get_discount(product_name):
                try:
                    return self.discounts.get(product_name) / 100
                except TypeError:
                    for item in self.stock:
                        if item.get(product_name):
                            type_name = item.get('type')
                            return self.discounts.get(type_name) / 100
                return 1

            price = self.pricelist.get(product_name)
            discount = - round(get_discount(product_name) * price, 2)
            cash_in = round((price - discount) * amount, 2)
            cos = round((price / self.PREMIUM) * amount, 2)
            gross_income = round(cash_in - cos, 2)
            return self.sales.append((product_name, amount, price, discount, cash_in, gross_income))

        for item in self.stock:
            if item.get(product_name):
                if item.get(product_name) < amount:
                    raise ValueError(f'stock left: {item.get(product_name)}')
                balance = item[product_name] - amount
                checkout(product_name, amount)
                return item.update({product_name: balance})
        raise ValueError('No product found')

    def get_product_info(self, product_name):  # returns a tuple with product name and amount of items in the store.
        for item in self.stock:
            if item.get(product_name):
                return product_name, item[product_name]
        raise ValueError('No product found')

    def get_income(self):  # returns amount of money earned by ProductStore instance.
        cash_in = 0
        gross_income = 0
        print('- ' * 20)
        for sales in self.sales:
            print(f'{sales[0]}: {sales[4]} = {sales[1]} * ({sales[2]} - {sales[3]})')
            cash_in += sales[4]
            gross_income += sales[5]
        print('- ' * 20)
        print(f'Gross income: {round(gross_income, 2)}')
        return cash_in

    def get_all_products(self):  # returns information about all available products in the store.
        return self.stock


p1 = Product('Sport', 'Football T-Shirt', 100)
p2 = Product('Food', 'Ramen', 1.5)

s = ProductStore()

s.add(p1, 10)
s.add(p2, 300)
print(s)

print('\n** discount and sale **')
s.set_discount('Food', 20)
s.sell_product('Ramen', 10)

s.set_discount('Ramen', 50)
s.sell_product('Ramen', 10)
print(s.get_product_info('Ramen'))
print(s)

print('\n** info **')
print(s.get_all_products())
print(s.get_income())

print('\n--- Task 4 ---\n')  # Custom exception
# Create your custom exception named `CustomException`,
# you can inherit from base Exception class, but extend its functionality to log every error message to a file named `logs.txt`.
# Tips: Use __init__ method to extend functionality for saving messages to file


class CustomException(Exception):

    def __init__(self, text):
        self.text = text
        with open('errors.txt', 'a+') as errors:
            errors.write(text)
