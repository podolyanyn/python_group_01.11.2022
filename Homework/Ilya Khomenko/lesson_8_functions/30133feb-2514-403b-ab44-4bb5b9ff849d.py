#Task-1
#def favourite_movie(name):
#    return (f'My favorite movie is named {name}')

#print(favourite_movie('school'))

#Task-2

#def make_country(name,capital):
#    x = {name:capital}
#    return x

#print(make_country("Ukraine",'Kyiv'),make_country('USA','Washington'))

#Task-3
#def make_operation(operator,number):
#    digits = []
#    while number:
#        digits += [number % 10]
#        number //= 10
#        i = digits[::-1] or [0]
#    if operator == '+':
#       add = int(i[0]+i[1]+i[2])
#       print(add)
#    if operator == '-':
#       minus = int(i[0]-i[1]-i[2])
#       print(minus)
#    if operator == '*':
#        multi = int(i[0]*i[1]*i[2])
#        print(multi)

#print(make_operation('*',1234))



def make_operations_1(operator,*number):
    result = 0
    if operator == '+':
        for num in number:
            result = result + num
        return result
    if operator == '-':
        for num in number:
            result = -num-result
        return result
    if operator == '*':
        result = 1
        for num in number:
            result = num*num
            return result

print(make_operations_1('*',7,6))