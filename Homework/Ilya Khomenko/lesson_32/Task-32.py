import time


def time_decorator(func):
    def wrapper(x):
        start = time.time()
        func(x)
        finish = time.time()
        print("Process time:", (finish - start) * 1000)

    return wrapper


# Task-1
# def two_dir_bubble_sort(my_list):
#     up = 0
#     down = 0
#     r = True
#
#     for index in range(len(my_list)-1,0,-1):
#         if r:
#             r = False
#             for indx in range(up,index+down,1):
#                 if my_list[indx] > my_list[indx+1]:
#                     my_list[indx],my_list[indx+1] = my_list[indx+1],my_list[indx]
#             up += 1
#         else:
#             r = True
#             for indx in range(index-1+up,down,-1):
#                 if my_list[indx] < my_list[indx-1]:
#                     my_list[indx],my_list[indx-1] = my_list[indx-1],my_list[indx]
#             down += 1
#     return my_list
#
# alist = [54,26,93,17,77,31,44,55,20]
# two_dir_bubble_sort(alist)
# print(alist)


# Task-2
def merge(arr, l, m, r):
    n1 = m - l + 1
    n2 = r - m

    L = [0] * (n1)
    R = [0] * (n2)

    for i in range(0, n1):
        L[i] = arr[l + i]

    for j in range(0, n2):
        R[j] = arr[m + 1 + j]

    i = 0
    j = 0
    k = l

    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1

    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1

    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1


def mergeSort(arr, l, r):
    if l < r:
        m = l + (r - l) // 2

        mergeSort(arr, l, m)
        mergeSort(arr, m + 1, r)
        merge(arr, l, m, r)


arr = [12, 11, 13, 5, 6, 7]
n = len(arr)
mergeSort(arr, 0, n - 1)
print("Відсортований масив")
for i in range(n):
    print("%d" % arr[i], end=" ")
# Task-3
import random

myList1 = [random.randint(0, 999) for _ in range(10)]
myList2 = [random.randint(0, 999) for _ in range(50)]
myList3 = [random.randint(0, 999) for _ in range(100)]
myList4 = [random.randint(0, 999) for _ in range(1000)]
myList5 = [random.randint(0, 999) for _ in range(10000)]
myList6 = [random.randint(0, 999) for _ in range(100000)]
myList7 = [random.randint(0, 999) for _ in range(1000000)]


@time_decorator
def quickSort(alist):
    quickSortHelper(alist, 0, len(alist) - 1)


def quickSortHelper(alist, first, last):
    if first < last:
        splitpoint = partition(alist, first, last)

        quickSortHelper(alist, first, splitpoint - 1)
        quickSortHelper(alist, splitpoint + 1, last)


def partition(alist, first, last):
    pivotvalue = alist[first]

    leftmark = first + 1
    rightmark = last

    done = False
    while not done:

        while leftmark <= rightmark and alist[leftmark] <= pivotvalue:
            leftmark = leftmark + 1

        while alist[rightmark] >= pivotvalue and rightmark >= leftmark:
            rightmark = rightmark - 1

        if rightmark < leftmark:
            done = True
        else:
            temp = alist[leftmark]
            alist[leftmark] = alist[rightmark]
            alist[rightmark] = temp

    temp = alist[first]
    alist[first] = alist[rightmark]
    alist[rightmark] = temp

    return rightmark

# quickSort(myList1)
# quickSort(myList2)
# quickSort(myList3)
# quickSort(myList4)
# quickSort(myList5)
# quickSort(myList6)


# print(myList1)
# print(myList2)
# print(myList3)
# print(myList4)
# print(myList5)
# print(myList6)
