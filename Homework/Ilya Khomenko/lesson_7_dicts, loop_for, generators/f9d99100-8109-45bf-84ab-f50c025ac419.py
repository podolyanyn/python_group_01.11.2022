#Task-1
#str_input = input('Введіть речення')
#counts = dict()
#words = str_input.split()

#for word in words:
#    if word in counts:
#        counts[word] += 1
#    else:
#         counts[word] = 1

#print(counts)

#Task-2

stock = {"banana": 6,"apple": 0,"orange": 32,"pear": 15}
prices = {"banana": 4,"apple": 2,"orange": 1.5,"pear": 3}
start = 0
for x in prices:
    total = prices[x] * stock[x]
    start +=total
print(start)


#Task-3
#list_variable = [(i,i*i) for i in range(1,11)]
#print(list_variable)

#Task-4
#list_days = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
#dict_days = {i:list_days[i] for i in range(0,len(list_days))}
#reverse_dict_days = {list_days[i]:i for i in range(0,len(list_days))}

#print(list_days)
#print(dict_days)
#print(reverse_dict_days)