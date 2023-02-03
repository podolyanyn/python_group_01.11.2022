from typing import List, Tuple


# We assume that all lists passed to functions are the same length N

def question1(first_list: List[int], second_list: List[int]) -> List[int]:
    res: List[int] = []  # O(1)
    for el_first_list in first_list:  # O(n)
        if el_first_list in second_list:  # O(n)
            res.append(el_first_list)  #O(n)
    return res  #O(1)

# Answer 1: O(n)


def question2(n: int) -> int:
    for _ in range(10):
        n **= 3
    return n
# Answer 2: O(1)


def question3(first_list: List[int], second_list: List[int]) -> List[int]:
    temp: List[int] = first_list[:]
    for el_second_list in second_list:
        flag = False
        for check in temp:
            if el_second_list == check:
                flag = True
                break
        if not flag:
            temp.append(second_list)
    return temp
# Answer 3: O(n^2)


def question4(input_list: List[int]) -> int:
    res: int = 0
    for el in input_list:
        if el > res:
            res = el
    return res
# Answer 4: O(n)


def question5(n: int) -> List[Tuple[int, int]]:
    res: List[Tuple[int, int]] = []
    for i in range(n):
        for j in range(n):
            res.append((i, j))
    return res
# Answer 5: O(n^2)


def question6(n: int) -> int:
    while n > 1:
        n /= 2
    return n
# Answer 6: O(log n)
