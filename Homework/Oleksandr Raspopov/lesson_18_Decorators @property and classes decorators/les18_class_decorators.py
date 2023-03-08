print('> > > Task 1 (e-mail validator)\n')
# Create a class method named `validate`, which should be called from the `__init__` method to validate parameter
# email, passed to the constructor.
# The logic inside the `validate` method could be to check if the passed email parameter is a valid email string.
# Valid email address format:
# https://help.xmatters.com/ondemand/trial/valid_email_format.htm
# Email address:
# https://en.wikipedia.org/wiki/Email_address


class Email:
    def __init__(self, email):
        Email.validate(str(email))

    @classmethod
    def validate(cls, email):
        import re

        def prefix(value):
            pattern = r'(^[-\w.])'
            char = r""" !"#$%&'()*+,-./:;<=>?[\]^_`{|}~"""
            if re.match(pattern, value)\
                    and ('#' not in value)\
                    and ('..' not in value)\
                    and (value[0] not in char)\
                    and (value[-1] not in char)\
                    and 0 < len(value) < 65:
                return True

        def domain(value):
            pattern = r'(([A-z0-9][-A-z0-9]+\.)+[A-z]{2,4}$)'
            if re.match(pattern, value) and 3 < len(value) < 64:
                return True

        split = email.split('@')
        if len(split) == 2 and prefix(split[0]) and domain(split[1]):
            print(f'OK: {email}')
        else:
            print(f'Invalid syntax: {email}')


invalid_prefix = ['abc-@mail.com', 'abc..def@mail.com', '.abc@mail.com', 'abc#def@mail.com']
invalid_domain = ['abc.def@mail.c', 'abc.def@mail#archive.com', 'abc.def@mail', 'abc.def@mail..com']
valid_prefix = ['abc-d@mail.com', 'abc.def@mail.com', 'abc@mail.com', 'abc_def@mail.com']
valid_domain = ['abc.def@mail.cc', 'abc.def@mail-archive.com', 'abc.def@mail.org', 'abc.def@mail.com']

for test in invalid_prefix:
    print('(-)', end=''), Email(test)
for test in invalid_domain:
    print('(-)', end=''), Email(test)
for test in valid_prefix:
    print('(+)', end=''), Email(test)
for test in valid_domain:
    print('(+)', end=''), Email(test)

print('\n> > > Task 2 (Boss & Worker)\n')


# Implement 2 classes, the first one is the Boss and the second one is the Worker.
# Worker has a property 'boss', and its value must be an instance of Boss.
# You can reassign this value, but you should check whether the new value is Boss.
# Each Boss has a list of his own workers. You should implement a method that allows you to add workers to a Boss.
# You're not allowed to add instances of Boss class to workers list directly via access to attribute, use getters and setters instead!
#
# You can refactor the existing code.
# id_ - is just a random unique integer


class Boss:
    def __init__(self, id_: int, name: str, company: str):
        self.id = id_
        self.name = name
        self.company = company
        self.workers = []

    def __str__(self):
        return f'> {self.name} (id: {self.id}, company: {self.company}), workers: {[workers.name for workers in self.workers]}'


class Worker:
    def __init__(self, id_: int, name: str, company: str, boss: Boss):
        self.id = id_
        self.name = name
        self.company = company
        self.boss = boss
        self.undercover = False

    @property
    def boss(self):
        return self._boss

    @boss.setter
    def boss(self, boss: Boss):
        if boss.__class__.__name__ != Boss.__name__:
            raise TypeError('boss must be "Boss" class instance')
        Worker._upd_ex_boss_list(self)
        self._boss = boss
        boss.workers.append(self)
        if boss.company != self.company:
            self.undercover = True

    @boss.deleter
    def boss(self):
        Worker._upd_ex_boss_list(self)
        self._boss = None
        print(f'> No boss of {self.name}')

    def _upd_ex_boss_list(self):
        try:
            self._boss.workers.remove(self)
        except AttributeError:
            pass

    def __str__(self):
        if self.boss is None:
            return f'> {self.name} (id: {self.id}, company: {self.company}, boss: {None}, undercover: {self.undercover})'
        else:
            return f'> {self.name} (id: {self.id}, company: {self.company}, boss: {self.boss.name}, undercover: {self.undercover})'


print('Set new instances:')
boss1 = Boss(1, 'M', 'MI6')
boss2 = Boss(2, 'Ernst Blofeld', 'Spectre')
worker1 = Worker(0o07, 'James Bond', 'MI6', boss1)
worker2 = Worker(0o1010001, 'Q', 'MI6', boss1)
worker3 = Worker(3, 'Moneypenny', 'MI6', boss1)
print(worker1)
print(boss1)

print('\nUpdate boss:')
worker2.boss = boss2
print(worker2)
print(boss2)
print(boss1)

print('\nGoodbye boss:')
del worker2.boss
print(worker2)
print(boss2)

print('\nTest ex boss list update:')
worker2.boss = boss2
print(worker2)
print(boss2)

# print('Invalid boss update:')
# worker2.boss = worker1
# print(worker2)

print('\n> > > Task 3 (Type convertor)\n')


# Write a class TypeDecorators which has methods for converting results of functions to a specified type (if possible):
# methods:
# to_int
# to_str
# to_bool
# to_float
# Don't forget to use @wraps


class TypeDecorators:
    from functools import wraps

    @staticmethod
    def to_str(func):
        @TypeDecorators.wraps(func)
        def to_str_arg(args):
            return str(args)
        return to_str_arg

    @staticmethod
    def to_bool(func):
        @TypeDecorators.wraps(func)
        def to_bool_arg(args):
            return bool(args)
        return to_bool_arg

    @staticmethod
    def to_int(func):
        @TypeDecorators.wraps(func)
        def to_int_arg(args):
            try:
                return int(args)
            except ValueError:
                return 'ValueError'
        return to_int_arg

    @staticmethod
    def to_float(func):
        @TypeDecorators.wraps(func)
        def to_int_arg(args):
            try:
                return float(args)
            except ValueError:
                return 'ValueError'
        return to_int_arg


@TypeDecorators.to_int
def do_nothing(string: str):
    return string
print(f"to_int 25: {do_nothing('25')}, {type(do_nothing('25'))}")
print(f"to_int 'False': {do_nothing('False')}, {type(do_nothing('False'))}")  # Test converting wrong format
assert do_nothing('25') == 25


@TypeDecorators.to_bool
def do_something(string: str):
    return string
print(f"to_bool 'True': {do_something('True')}, {type(do_something('True'))}")
assert do_something('True') is True


# @TypeDecorators.to_str
# def do_something(string):
#     return string
# print(f"to_str True: {do_something(True)}, {type(do_something(True))}")


# @TypeDecorators.to_float
# def do_something(string):
#     return string
# print(f"to_float 25: {do_something('25')}, {type(do_something('25'))}")
# print(f"to_float 'False': {do_something('False')}, {type(do_something('False'))}")  # Test converting wrong format
