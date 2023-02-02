import enum
#Task-1

class Pesron():
    def __init__(self,name,surname,age,character):
        self.name = name
        self.surname =  surname
        self.age = age
        self.character = character
        print(f'{name},{surname},{age},{character}')

class Student(Pesron):
    def __init__(self,name,surname,age,excellent_student,character,c_be_teacher):
        super().__init__(self,name,surname,age,character)
        self.excellent_student = excellent_student
        self.c_be_teacher = c_be_teacher
        print(f'{name},{surname},{age},{excellent_student},{c_be_teacher}')

    def do_homework(name,surname,age,excellent_student,character,c_be_teacher):
        if excellent_student == True:
            print(f'{name},{surname},{age},{excellent_student},{c_be_teacher}')
            print('Yes')
        else:
            print(f'{name},{surname},{age},{excellent_student},{c_be_teacher}')
            print('No')

class Teacher(Pesron):
    def __init__(self,name,surname,age,character,sallary,teacher,work_day_end):
        super().__init(self,name,surname,age,character,sallary)
        self.sallary = sallary
        self.teacher = teacher
        print(f'{name},{surname},{age},{sallary},{teacher}')

    def check_homework(name,surname,age,character,sallary,teacher,work_day_end):
        if work_day_end == True:
            print(f'{name},{surname},{age},{character},{teacher},{work_day_end}')
            print('Yes')
        else:
            print(f'{name},{surname},{age},{character},{teacher},{work_day_end}')
            print('No')



Pesron('Illja','Homenko',18,'good')
Student.do_homework('Illja','Homenko',18,True,'good',False)
Teacher.check_homework('Illja','Homenko',40,'bad',4600,True,False)

#Task-2

class Mathematician:

    def square_nums(self,*args):
        for x in args:
            print([y**2 for y in x])

    def remove_positives(self,*args):
        for x in args:
            print([y for y in x if y <= 0])
    
    def filter_leaps(self,*args):
        for x in args:
            print([y for y in x if  y%4 ==0 and y%100 != 0 or y%400 == 0])


m = Mathematician()

m.square_nums([7, 11, 5, 4]) 

m.remove_positives([26, -11, -8, 13, -90]) 

m.filter_leaps([2001, 1884, 1995, 2003, 2020]) 



#Task-3
class Product:
    def __init__(self,type,name,price)->list:
        self.type = type
        self.name = name
        self.price = price
        self.prem = (0.3*self.price)

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
    







p = Product('Sport','Football T-Shirt',100)
p1 = Product('Food', 'Ramen', 20)
p2 = Product('Sport', 'Ball', 50)
s = ProductStore()
s.add(p,10)
s.add(p1, 300)
s.add(p2, 200)
s.set_discount('Sport',10,'Football T-Shirt')
s.set_discount('Food',20,'Ramen')
s.set_discount('Sport',5,'Ball')
s.sell_product('Ramen',10)
s.sell_product('Ball',99)
s.sell_product('Football T-Shirt',8)
s.get_income()
s.get_all_products()
s.get_product_info('Football T-Shirt')
s.get_product_info('Ramen')
s.get_product_info('Ball')




#Task-4

class CustomExceptoin(Exception):
    def __init__(self,error,message):
        self.error = error
        self.message = message
        message = error
        super().__init__(self.message)
        with open('log.txt','a+') as f:
            f.write(self.message)





