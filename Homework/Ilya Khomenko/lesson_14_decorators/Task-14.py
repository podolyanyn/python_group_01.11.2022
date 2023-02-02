#Task-1
def logger(func):
    def wrap(*args):
        name = func.__name__
        called_args = ', '.join(str(x) for x in args)
        print(f'Called {name} with args {called_args}')
    return wrap
  
  
@logger
def add(x,y):
    return x + y

@logger
def square_all(*args):

    return [arg ** 2 for arg in args]

add(1,2)
add(10, 22)
add(10, 2)


square_all(10,2,1,22)


#Task-2
def stop_words(words):
    def wrapper(func):
        def inwrapper(name):
            string = func(name)
            for char in words:
                string = string.replace(char, "*")
            print(string)
        return inwrapper
    return wrapper


@stop_words(['BMW','pepsi'])
def create_slogan(name) -> str:

    return f"{name} drinks pepsi in his brand new BMW!"

print(create_slogan('Illja'))


#Task-3

def agr_rules(type_,max_length,contains):
    def wrapper(func):
        def inwrapper(name):
            for x in contains:
                if type(name) == type_ and len(name) <= max_length and x in name:
                    print(func(name))
                else:
                    if type(name) != type_:
                        print('Invalid type')

                    elif len(name) <= max_length:
                        print('Invalid length')

                    else:
                        print('Lack of matching symbols')
                    return False
        return inwrapper
    return wrapper


@agr_rules(type_=str,max_length=15,contains=['05','@'])
def create_slogan(name: str) -> str:

    return f"{name} drinks pepsi in his brand new BMW!"  



create_slogan('S@SH05')
create_slogan('johndoe05@gmail.com')
