#task_1 = task_2
# щодо другого завдання - я не певен чи я правильно його зрозумів, але наче як у першому я виконав умову й другого
# напишіть будь ласка якщо я помиляюся

def func(func):
    def wrap():
        return f"The number of local variables is {func.__code__.co_nlocals}"
    return wrap

@func
def f():
    a, b, c = 1, 2, 3
    return a + b + c

@func
def ff():
    t, q, h, a, g, e, s, d = 2, 5, 2, 4, 2, 1, 3, 5
    return None

print(f())
print(ff())

#task_3

def choose_func(nums: list, func1, func2):
    for num in nums:
        if num < 0:
            return func2(nums)
    return func1(nums)


# Assertions

nums1 = [1, 2, 3, 4, 5]

nums2 = [1, -2, 3, -4, 5]


def square_nums(nums):
    return [num ** 2 for num in nums]

def remove_negatives(nums):
    return [num for num in nums if num > 0]

print(choose_func(nums1, square_nums, remove_negatives))
print(choose_func(nums2, square_nums, remove_negatives))

