from random import randint
from typing import List


# O(n^2)
def bubble_sort(arr: List[int]) -> List[int]:
    up = True
    low = 0
    high = len(arr)-1
    while low < high:
        if up is True:
            for i in range(low, high, 1):
                if arr[i] > arr[i+1]:
                    arr[i+1], arr[i] = arr[i], arr[i+1]
            high -= 1
            up = False
        else:
            for i in range(high, low, -1):
                if arr[i] < arr[i-1]:
                    arr[i-1], arr[i] = arr[i], arr[i-1]
            low += 1
            up = True
    return arr


if __name__ == '__main__':
    items = [2, 4, 1, 3, 5, 7, 6, 9, 8, 0]
    lst = [randint(1, 100) for _ in range(20)]
    print("bubble_sort: (items)", bubble_sort(items))
    print("bubble_sort: (random)", bubble_sort(lst))
