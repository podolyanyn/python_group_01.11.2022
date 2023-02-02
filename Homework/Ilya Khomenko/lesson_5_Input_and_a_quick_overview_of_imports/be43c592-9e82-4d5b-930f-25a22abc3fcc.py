import random
#Task-1
list1 = random.sample(range(100), 10)
i = 0
max = list1[0]
while i < len(list1)-1:
    if max > list1[i+1]:
        pass
    else:
        max = list1[i+1]
    i+=1
print('Max number: ', max)

#Task-2
list2 = random.sample(range(10), 10)
list3 = random.sample(range(10), 10)

c = set(list2) & set(list3)  
print(c)

#Task-3
list4 = random.sample(range(1,100), 10)
print(list4)
i = 0
max = list4[0]
while i < len(list4)-1:
    if (i%7==0) and (i%5!=0):
       list4.append(i)
    i+=1
print(max)











