from random import randint
from typing import List


# O(n log n)
def insertion_sort(arr: List[int], low, high) -> List[int]:
    for i in range(low + 1, high + 1):
        val = arr[i]
        j = i
        while j > low and arr[j - 1] > val:
            arr[j] = arr[j - 1]
            j -= 1
        arr[j] = val
    return arr


def partition(arr: List[int], low, high) -> int:
    pivot = arr[high]
    j = low
    for i in range(low, high):
        if arr[i] < pivot:
            arr[i], arr[j] = arr[j], arr[i]
            j += 1
    arr[j], arr[high] = arr[high], arr[j]
    return j


def quick_sort(arr: List[int], low, high) -> List[int]:
    if low < high:
        pivot = partition(arr, low, high)
        quick_sort(arr, low, pivot - 1)
        quick_sort(arr, pivot + 1, high)
        return arr


def advanced_quick_sort(arr, low, high) -> List[int]:
    while low < high:
        if high - low + 1 < 10:
            insertion_sort(arr, low, high)
            break
        else:
            pivot = partition(arr, low, high)
            if pivot - low < high - pivot:
                quick_sort(arr, low, pivot - 1)
                low = pivot + 1
            else:
                quick_sort(arr, pivot + 1, high)
                high = pivot - 1
    return arr


if __name__ == '__main__':
    items = [2, 4, 1, 3, 5, 7, 6, 9, 8, 0]
    lst = [randint(1, 100) for _ in range(20)]
    print("quick sort: (items)", advanced_quick_sort(items, 0, len(items)-1))
    print("quick sort: (random)", advanced_quick_sort(lst, 0, len(lst)-1))
