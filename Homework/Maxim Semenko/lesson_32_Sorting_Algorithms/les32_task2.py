from random import randint
from typing import List


# 0(n log n)
def merge(arr: List[int], start: int, mid: int, end: int) -> None:
    start2 = mid + 1
    if arr[mid] <= arr[start2]:
        return
    while start <= mid and start2 <= end:
        if arr[start] <= arr[start2]:
            start += 1
        else:
            value = arr[start2]
            index = start2
            while index != start:
                arr[index] = arr[index - 1]
                index -= 1
            arr[start] = value
            start += 1
            mid += 1
            start2 += 1


def merge_sort(arr: List[int], left: int, right: int) -> List[int]:
    if left < right:
        m = left + (right - left) // 2
        merge_sort(arr, left, m)
        merge_sort(arr, m + 1, right)
        merge(arr, left, m, right)
    return arr


if __name__ == '__main__':
    items = [2, 4, 1, 3, 5, 7, 6, 9, 8, 0]
    lst = [randint(1, 100) for _ in range(20)]
    print("merge_sort: (items)", merge_sort(items, 0, len(items)-1))
    print("merge_sort: (random)", merge_sort(lst, 0, len(lst)-1))
