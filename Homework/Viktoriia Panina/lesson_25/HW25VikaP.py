from typing import Optional,Tuple

def question1(first_list: list[int], second_list: list[int]) -> list[int]:
    res: list[int] = []
    for el_first_list in first_list: # >> here cycle runs n time
        if el_first_list in second_list: # >> since this is not another cycle, same n of operations are performed
            res.append(el_first_list)
    return res

# Since this operation is linear, we may assume that this O(n).
#Answer = n

#task 2
def question2(n: int) -> int:
    for _ in range(10): # >> means that the cycle will be running for each number in from 0 to 9
        n **= 3
    return n
# Since we now how many times the cycle will be running, notation is constant here.
#Answer = 10

#task 3
def question3(first_list: list[int], second_list: list[int])-> list[int]: # >> as it was mentioned in the task all lists are N lenghts, so we assigning them to the same variable n
   temp: list[int] = first_list[:]
   for el_second_list in second_list: # >> n operations will be run
      flag = False
      for check in temp: # >> another n running inside the cycle
         if el_second_list == check:
            flag = True
            break
      if not flag:
         temp.append(second_list)
   return temp

#Since there is nested for in cycle we may assume that this function is quadratic compelxity
# Answer - n^2

#task 4
def question4(input_list: list[int]) -> int:
  res: int = 0
  for el in input_list: # >> cycle will be running n times
    if el > res:
      res = el
  return res

#This is also a function with linear complexity, since it is running the cycle n-times
# Answer - n

#task 5
def question5(n: int) -> list[Tuple[int, int]]:
    res: list[Tuple[int, int]] = []
    for i in range(n): # >> the opeation will be running n-times
        for j in range(n): # >> same here: operation will be repeated n-times
            res.append((i, j))
    return res
#This function with quadratic complexity
#Aswer - n^2

#task 6
def question6(n: int) -> int:
    while n > 1:
        n /= 2
    return n
# this fundting will be dividing n by 2, until it is equal to or less than 1.
# it means that Big O is n as it depends on n




