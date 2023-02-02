#Task-1
def str_manipulation(str):
  if len(str) < 2:
    return 'Empty String'

  return str[0:2] + str[-2:]

print(str_manipulation('helloworld'))
print(str_manipulation('my'))
print(str_manipulation('x'))

#Task-2
a = str(input("Enter a number: "))
if a.isdigit() and len(a) == 10:
    print('Valid')
else:
    print('Invalid')

#Task-3
menu = {
    "1": 'Додавання',
    '2': 'Віднімання',
    '3': 'Множення',
    '4': 'Ділення',
    '5': 'Вихід' 
}
print(menu)

option=int(input("Виберіть число для операції: "))
while option > 5 or option <= 0:
    print("Invalid menu option.")
    option = int(input("Оберіть правильне число: "))


while option!=5:

  number1=int(input('Введіть число 1: '))
  number2=int(input('Введіть число 2: '))
  if option==1:
    correctAnsswer=number1+number2
    
    userAnswer=int(input(f"{number1} + {number2} = "))
    
    if userAnswer==correctAnsswer:
      print("Правильно!")
      
    else:
      print("наступного разу повезе")
      
  elif option==2:
    correctAnsswer=number1-number2
    
    userAnswer=int(input(f"{number1} - {number2} = "))
  
    if userAnswer==correctAnsswer:
      print("Правильно!")
      
    else:
      print("наступного разу повезе")
      
  elif option==3:
    correctAnsswer=number1*number2
   
    userAnswer=int(input(f"{number1} x {number2} = "))

    if userAnswer==correctAnsswer:
      print("Правильно!")
      
    else:
      print("наступного разу повезе")
      
  elif option==4:
    correctAnsswer=number1/number2

    userAnswer=int(input(f"{number1} / {number2} = "))
  
    if userAnswer==correctAnsswer:
      print("Правильно!")
    else:
        print("наступного разу повезе")
        


#Task-4
const_name = 'illya'

input_name = str(input("Введіть ім'я: "))
print(const_name == input_name.lower())



