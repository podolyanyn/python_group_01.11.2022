#Task-1
import re
class Check:

    def __init__(self,email):
        type(self).validate(email)
        self.email = email


    @classmethod
    def validate(cls, email):
        if not re.match(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)", email):
            raise TypeError(f'Email {email} is invalid')


#email1 = Check('test@gmail.com')
#email2 = Check('Illja2004@mail.com')
#email3 = Check('Johnygmail.com')
#email4 = Check('illja.com')

#Task-2
class Boss:
    def __init__(self,id_:int,name:str,company:str):
        self.id = id_
        self.name = name
        self.company = company
        self._workers = []

    @property
    def workers(self):
        return self._workers
    
    @workers.setter
    def workers(self,worker):
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
    def Boss(self,boss):
        if isinstance(boss,Boss):
            self._Boss = boss
        else:
            raise TypeError("Error")



#Task-3
class TypeDecorators:

    @staticmethod
    def do_noth(string):
        return string

    @staticmethod
    def to_int(string):
        return int(string)

    @staticmethod
    def to_float(string: str):
        return float(string)
    
    @staticmethod
    def to_bool(string: str):
        return bool(string)

    @staticmethod
    def to_string(string: str):
        return str(string)

    
print(TypeDecorators.to_int('25') == 25)
print(TypeDecorators.to_bool('True') is True)
print(TypeDecorators.to_string(135) == "135")
print(TypeDecorators.to_float(20) == 20.0)