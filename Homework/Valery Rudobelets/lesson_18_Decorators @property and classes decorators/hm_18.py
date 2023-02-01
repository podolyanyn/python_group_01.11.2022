import re

# task_1

regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'


class Validator:

    def __init__(self, mail):
        self._mail = mail
        self.validate_result = self.validate(mail)

    def validate(self, mail):
        if re.fullmatch(regex, mail):
            return True
        else:
            return False


validator = Validator("abcdef@mail.com")
print(validator.validate_result)

# task_2


class Boss:

    def __init__(self, id_: int, name: str, company: str):
        self.id = id_
        self.name = name
        self.company = company
        self._workers = []

    @property
    def all_workers(self):
        return self._workers

    @all_workers.setter
    def all_workers(self, worker):
        self._workers.append(worker)


class Worker:

    def __init__(self, id_: int, name: str, company: str, boss: Boss):
        self.id = id_
        self.name = name
        self.company = company
        self._boss = boss

    @property
    def boss(self):
        return self._boss

    @boss.setter
    def boss(self, boss):
        if isinstance(boss, Boss):
            self._boss = boss
        else:
            raise TypeError("That's not a Boss instance")


boss1 = Boss(1, "John Johnson", "Roshen")
boss2 = Boss(2, "Carl Carlson", "Millenium")
worker1 = Worker(11, "Name Nameson", "Roshen", boss1)
worker2 = Worker(12, "Worker Workerson", "Millenium", boss2)
worker3 = Worker(13, "Dima", "Roshen", boss1)
worker4 = Worker(14, "Valera", "Millenium", boss2)

boss1._workers = [worker1, worker3]

# print(boss1._workers)

# worker1.boss = "boss2"
# print(worker1.boss)
# task_3


class TypeDecorators:

    @staticmethod
    def do_nothing(string: str):
        return string

    @staticmethod
    def to_int(string: str):
        return int(string)

    @staticmethod
    def to_bool(string: str):
        return bool(string)

    @staticmethod
    def to_string(string: str):
        return str(string)

    @staticmethod
    def to_float(string: str):
        return float(string)

    print(to_int('25') == 25)
    print(to_bool('True') is True)
    print(to_string(135) == "135")
    print(to_float(20) == 20.0)