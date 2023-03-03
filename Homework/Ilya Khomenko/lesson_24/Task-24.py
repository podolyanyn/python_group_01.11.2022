#Task-1
from typing import Optional
w = [int,float]
def to_power(x, exp) :
   if(exp==1):
       return(x)
   elif exp <0:
       raise ValueError("This function works only with exp > 0.")
   if(exp!=1):
       return(x*to_power(x,exp-1))



print("Result:",to_power(2,3))       

#Task-2
def is_palindrome(looking_str: str, index: int = 0) -> bool:
    if len(looking_str) == 1:
        return True
    else:
        return is_palindrome(looking_str[index]) ==is_palindrome(looking_str[index])


#Task-3
def mult(a:int, n:int )->int:
    if n == 0:
        return 0
    elif n <0:
        return - (a - mult(a,n+1))
    else:
        return a + mult(a,n-1)


if __name__ == '__main__':
    print("3 * 2 = " ,mult(3,2))
    print("3 * (-2) = ",mult(3,-2))
    print("(-3) * 2 = ",mult(-3,2))
    print("(-3) * (-2)= ",mult(-3,-2))

#Task-4
def reverse(input_str: str) -> str:
    if input_str == "":
        return input_str
    else:
        return reverse(input_str[1:]) + input_str[0]
   
             
if __name__ == '__main__':
    print("Hello" ,reverse('Hello'))
    print("Python",reverse("Python"))
    print("o",reverse('o'))

#Task-5
def sum_of_digits(digit_string: str) -> int:

    if digit_string == 0:
        return 0
    return (digit_string % 10 + sum_of_digits(int(digit_string / 10)))


num = '12345'
result = sum_of_digits(int(num))
print("Sum of digits in",num,"is", result) 