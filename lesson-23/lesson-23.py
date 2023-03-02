#Task-1
import re
class Check:

    def __init__(self,email)->str:
        type(self).validate(email)
        self.email = email


    @classmethod
    def validate(cls, email):
        if not re.match(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)", email):
            raise TypeError(f'Email {email} is invalid')


email1 = Check('test@gmail.com')
email2 = Check('Illja2004@mail.com')

#Task-2
#Done