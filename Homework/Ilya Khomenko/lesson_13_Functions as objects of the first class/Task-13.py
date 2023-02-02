#Task-1
def test():
    x = 1
    y = 2
    str1= "hello"


print(test.__code__.co_nlocals)



#Task-2
def test(a):
        def add(b):
                nonlocal a
                a += 1
                return a+b
        return add
func= test(20)
print(func(1))


#Task-3
nums1 = [1, 2, 3, 4, 5]

nums2 = [1, -2, 3, -4,5]


def choose_func(nums: list, func1,func2):
    if all(n>0 for n in nums):
        print(square_nums(nums))
    else:
        print(remove_negatives(nums))
    
def square_nums(nums):
    return [num ** 2 for num in nums]

             
def remove_negatives(nums):
    return [num for num in nums if num > 0]

choose_func(nums1,square_nums, remove_negatives)
choose_func(nums2,square_nums,remove_negatives)