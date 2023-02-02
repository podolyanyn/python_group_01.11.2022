#Task-1
import random 

x = random.randint(1,10)

user_input = int(input('Введіть число: '))
if x == user_input:
    print(f'Ви вгадали число: {x} ')
else:
    print(f'Ви не вгадали. Загадане число: {x}')

#Task-2
input_name = input("Введіть ім'я: ")
input_age = int(input('Введіть вік: '))
input_age += 1
print('Hello' + " " +  input_name +" "+'on your next birthday you’ll be'+ " "+ str(input_age) + " " +'years' )

#Task-3
input_str = input('Введіть рядок: ')



for i in range(5):
    result_str = ''.join(random.choice(input_str) for i in range(len(input_str)))
    print("Рядок:", result_str)