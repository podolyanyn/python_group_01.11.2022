#task_1

def logger(func):
    def wrap(*args):
        f = func.__name__
        s = ", ".join(str(x) for x in args)
        return f"{f} called with {s}"
    return wrap


@logger
def add(x, y):
    return x + y


@logger
def square_all(*args):
    return [arg ** 2 for arg in args]

print(add(2, 4))
print(square_all(1, 5, 2, 6, 1))

#task_2

def stop_words(words: list):
    def wrap(func):
        def inner(name):
            result = func(name)
            for i in range(len(words)):
                result = result.replace(words[i], '*')
            return result
        return inner
    return wrap

@stop_words(['pepsi', 'BMW'])
def create_slogan(name: str):
    return f"{name} drinks pepsi in his brand new BMW !"

print(create_slogan("Steve"))

#task_3

def arg_rules(type_: type, max_length: int, contains: list):
    def wrap(func):
        def inner(name):
            for i in contains:
                if len(name) > max_length:
                    return False
                elif i not in name:
                    return False
                elif type_ is not str:
                    return False
            return func(name)
        return inner
    return wrap


@arg_rules(type_=str, max_length=15, contains=['05', '@'])
def create_slogan(name: str) -> str:
    return f"{name} drinks pepsi in his brand new BMW!"


print(create_slogan('johndoe05@gmail.com'))

print(create_slogan('S@SH05'))
