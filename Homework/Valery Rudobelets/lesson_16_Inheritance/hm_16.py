# task_1

class Person:
    num_of_people = 0

    def __init__(self, first_name, last_name, age, school, city):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.school = school
        self.city = city
        self.full_name = f"{self.first_name} {self.last_name}"
        Person.num_of_people += 1

    def account(self):
        return {
            "Name": {self.full_name},
            "Age": self.age,
            "School": self.school,
            "City": self.city
        }

    def isadult(self):
        if self.age > 18:
            return f"{self.full_name} is adult"
        else:
            return f"{self.full_name} is a student"


class Student(Person):
    num_of_students = 0

    def __init__(self, first_name, last_name, age, school, city, grade, average_mark, parents):
        super().__init__(first_name, last_name, age, school, city)
        self.grade = grade
        self.average_mark = average_mark
        self.parents = parents
        Student.num_of_students += 1

    def account(self):
        return {
            "Name": f"{self.full_name}",
            "Age": self.age,
            "School": self.school,
            "Grade": self.grade,
            "Average Mark": self.average_mark,
            "Parents": self.parents,
            "City": self.city
        }

    def isable(self):
        if self.average_mark < 6:
            return f"{self.full_name} from {self.grade} needs to revise the whole program"
        elif self.average_mark < 10:
            return f"{self.full_name} is recommended to revise some of program"
        elif self.average_mark < 12:
            return f"{self.full_name} doesn't need to revise program"


class Teacher(Person):
    number_of_teachers = 0

    def __init__(self, first_name, last_name, age, school, city, salary_per_hour, week_hours, diploma):
        super().__init__(first_name, last_name, age, school, city)
        self.salary_per_hour = salary_per_hour
        self.diploma = diploma
        self.week_hours = week_hours
        self.total_salary = self.salary_per_hour * self.week_hours * 4

        Teacher.number_of_teachers += 1

    def account(self):
        return {
            "Name": f"{self.full_name}",
            "Age": self.age,
            "School": self.school,
            "City": self.city,
            "Diploma": self.diploma,
            "Salary": self.salary_per_hour*self.week_hours
        }

    def total_salary(self):
        if self.diploma:
            return f"The total salary of Mr/Mrs.{self.last_name} is {self.total_salary * 1.5}$"
        else:
            return f"The total salary of Mr/Mrs.{self.last_name} is {self.total_salary}$"


class Parents(Person):
    number_of_parents = 0

    def __init__(self, first_name, last_name, age, school, city, occupation, children):
        super().__init__(first_name, last_name, age, school, city)
        self.occupation = occupation
        self.children = children

        Parents.number_of_parents += 1

    def account(self):
        return {
            "Name": f"{self.full_name}",
            "Age": self.age,
            "School": self.school,
            "City": self.city,
            "Occupation": self.occupation,
            "Children": self.children
        }


stu_1 = Student("Noah", "Li", 10, "Central School", "Boston", "4-B", 11, ["Nick Li", "Helena Li"])
stu_2 = Student("Liam", "Li", 8, "Central School", "Boston", "2-A", 4, ["Nick Li", "Helena Li"])
stu_3 = Student("Mason", "Martin", 12, "Centennial School", "Toronto", "7-C", 5, ["Olivia Martin", "Emma Martin"])
stu_4 = Student("Jacob", "Martin", 7, "Centennial School", "Toronto", "2-B", 12, ["Olivia Martin", "Emma Martin"])
stu_5 = Student("William", "Martin", 9, "Centennial School", "Toronto", "5-B", 9, ["Olivia Martin", "Emma Martin"])
prt_1 = Parents("Nick", "Li", 30, "Central School", "Boston", "Web-developer", ["Noah Li", "Liam Li"])
prt_2 = Parents("Helena", "Li", 29, "Central School", "Boston", "UX-designer", ["Noah Li", "Liam Li"])
prt_3 = Parents("Olivia", "Martin", 35, "Centennial School", "Toronto", "Housewife", ["Mason Martin", "Jacob Martin",
                                                                                         "William Martin"])
prt_4 = Parents("Emma", "Martin", 28, "Centennial School", "Toronto", "Product-manager", ["Mason Martin",
                                                                                             "Jacob Martin",
                                                                                             "William Martin"])
tcr_1 = Teacher("Sophie", "Wilson", 45, "Centennial School", "Toronto", 20, 40, True)
tcr_2 = Teacher("Charlotte", "Smith", 23, "Centennial School", "Toronto", 15, 28, False)
tcr_3 = Teacher("Elizabeth", "Anderson", 68, "Central School", "Boston", 27, 30, True)


# print(Student.num_of_students)
# print(stu_1.account())

# task_2


class Mathematician:

    def square_nums(self, lst):
        return [i**2 for i in lst]

    def remove_positives(self, lst):
        return [i for i in lst if i < 0]

    def filter_leaps(self, lst):
        return


m = Mathematician()

# print(m.square_nums([7, 11, 5, 4]))
# print(m.remove_positives([26, -11, -8, 13, -90]))
# print(m.filter_leaps([2001, 1884, 1995, 2003, 2020]))

# task_3
# Я дещо не зрозумів це завдання, тому попросив поділитися пана Глущенка своїм рішенням. Я зрозумів що саме вимагалося
# але що малося на увазі під "преміум" я все ще не розумію. Мені сподобалося рішення яке тут надав автор, тож я вирішив
# не змінювати код кардинально, але доповнив дещо що я би змінив.


class Product:

    def __init__(self, product_type, name, price):
        self.product_type = product_type
        self.name = name
        self.price = price
        self.premium = round(0.3 * self.price, 1)


class ProductStore:

    def __init__(self):
        self.product_type = []
        self.product_name = []
        self.price = []
        self.premium = []
        self.amount = []
        self.income = 0

    def error(self, text="Unknown Error"):
        raise ValueError(text)

    def product_index(self, name):
        return self.product_name.index(name)

    def isavailable(self, name, amount=0):
        if name in self.product_name and self.amount[self.product_index(name)] >= amount:
            return True
        return False

    def add(self, name, amount):
        if not self.isavailable(name):
            self.product_type.append(name.product_type)
            self.product_name.append(name.name)
            self.price.append(name.price)
            self.premium.append(name.premium)
            self.amount.append(amount)
        else:
            self.amount[self.product_index(name)] += amount

    def set_discount(self, identifier, discount, identifier_type="name"):
        if identifier_type == 'name':
            if self.isavailable(identifier):
                i = self.product_index(identifier)
                delta = self.price[i] * (discount/100)
                self.premium[i] -= delta
                self.price[i] -= delta
            else:
                self.error(f'We do not sell "{identifier}"!')
        elif identifier_type == 'type' and identifier in self.product_type:
            for i, store_identifier in enumerate(self.product_type):
                if store_identifier == identifier:
                    delta = self.price[i] * (discount/100)
                    self.premium[i] -= delta
                    self.price[i] -= delta
        elif identifier not in self.product_type:
            self.error(f"'{identifier}' is a wrong type.")

    def sell(self, name, amount):
        if self.isavailable(name, amount):
            self.amount[self.product_index(name)] -= amount
            self.income += amount * self.premium[self.product_index(name)]
        elif self.amount[self.product_index(name)] == 0:
            self.error(f"There is no {name} left!")
        else:
            self.error(f"We don't have enough {name}, we've got only {self.amount[self.product_index(name)]} pieces.")

    def get_income(self):
        return self.income

    def get_all_product(self):
        output = f""
        for i in range(len(self.product_name)):
            output += f'{i + 1}) product type: {self.product_type[i]}, product name: {self.product_name[i]}, ' \
                      f'amount: {self.amount[i]}, price: {self.price[i]} UAH, premium per unit: {self.premium[i]} UAH' \
                      f' \n'
        return output

    def get_product_info(self, name):
        if self.isavailable(name):
            i = self.product_index(name)
            return self.product_name[i], self.amount[i]
        else:
            self.error(f'We do not have "{name}"!')


p1 = Product('Flowers', 'Cotton', 150)
p2 = Product('Flowers', 'Roses', 120)
p3 = Product('Food', 'Ramen', 165)
p4 = Product('Food', 'Shawarma', 80)
p5 = Product('Food', 'Sugar', 5)
p6 = Product('Drinks', 'Coffee', 50)
p7 = Product('Drinks', 'Tea', 25)
p8 = Product('Accessories', 'Candles', 3)
p9 = Product('Accessories', 'Big candles', 30)
p10 = Product('Drinks', 'Cecsi', 15)
p11 = Product('Drinks', 'Foca-Fola', 15)
p12 = Product('Food', 'Sushi', 300)

s = ProductStore()

s.add(p1, 7)
s.add(p2, 25)
s.add(p3, 15)
s.add(p4, 10)
s.add(p5, 200)
s.add(p6, 100)
s.add(p7, 100)
s.add(p8, 1000)
s.add(p9, 100)
s.add(p10, 75)
s.add(p11, 75)
s.add(p12, 15)
s.set_discount("Cotton", 15)
s.set_discount("Drinks", 15, "type")
# s.set_discount("Cars", 15, "type")
s.sell("Coffee", 2)
s.sell("Coffee", 1)
s.sell("Coffee", 3)
s.sell("Candles", 100)
s.sell("Candles", 100)
s.sell("Candles", 100)
s.sell("Candles", 100)
s.sell("Cotton", 5)

# print(s.income)
# print(s.get_product_info("Ramen"))
# print(s.get_all_product())


# task_4
# тут навіть не маю що додати

class CustomException(Exception):

    def __init__(self, msg: str):
        self.msg = msg
        with open('logs.txt', 'a+') as log:
            log.write(msg)


number_of_errors = 10
for i in range(number_of_errors, -1, -1):
    if i != 0:
        CustomException(f'...Critical error! Your PC will be self destroyed in {i} second{(i != 1) * "s"}!\n')
    else:
        CustomException(f'...Boom!\n')