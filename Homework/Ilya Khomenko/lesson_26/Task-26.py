#Task-1
class Stack():
    def __init__(self) -> None:
        self.items = list()
        self.size = -1

    def isEmpty(self):
        if self.size==-1:
            return True
        else:
            return False
    

    def pop(self):
        if self.isEmpty():
            print('Stack empty,create stack')
        else:
            self.size-=1
            return self.items.pop()
    def push(self,item):
        self.items.append(item)
        self.size+=1

    def reverse(self,string):
        n = len(string)
        for i in range(0,n):
            self.push(string[i])
        string = ""
        for i in range(0,n):
            string+=R.pop()
        return string

# R = Stack()
# line= input('Enter a string: ')
# seq = R.reverse(line)
# print(seq)
            
#Task-2
def parChecker(symbolString):
    s = Stack()
    balanced = True
    index = 0
    while index < len(symbolString) and balanced:
        symbol = symbolString[index]
        if symbol in "([{":
            s.push(symbol)
        else:
            if s.isEmpty():
                balanced = False
            else:
                top = s.pop()
                if not matches(top,symbol):
                       balanced = False
        index = index + 1
    if balanced and s.isEmpty():
        return True
    else:
        return False

def matches(open,close):
    opens = "([{"
    closers = ")]}"
    return opens.index(open) == closers.index(close)

# print(parChecker('{({([][])}())}'))
# print(parChecker('[{()]'))

#Task-3
# Python program to demonstrate
# stack implementation using a linked list.
# node class

class Node:
	def __init__(self, value):
		self.value = value
		self.next = None


class Stack:
    def __init__(self):
        self.head = Node("head")
        self.size = 0

    def __str__(self):
        cur = self.head.next
        out = ""
        while cur:
            out += str(cur.value) + "->"
            cur = cur.next
        return out[:-3]


    def getSize(self):
        return self.size


    def isEmpty(self):
        return self.size == 0


    def peek(self):
        if self.isEmpty():
            raise Exception("Peeking from an empty stack")
        return self.head.next.value

    def push(self, value):
        node = Node(value)
        node.next = self.head.next
        self.head.next = node
        self.size += 1


    def pop(self):
        if self.isEmpty():
            raise Exception("Popping from an empty stack")
        remove = self.head.next
        self.head.next = self.head.next.next
        self.size -= 1
        return remove.value

    def get_from_stack(self,x):
            current = self.head
            while current != None:
                if current.value == x:

                    return current.value
                
                current = current.next
                
            return Exception("Value not found!")
         




if __name__ == "__main__":
    stack = Stack()
    for i in range(1, 11):
        stack.push(i)
    print(f"Stack: {stack}")
    print(stack.get_from_stack(12))

    


    for _ in range(1, 6):
        remove = stack.pop()
        print(f"Pop: {remove}")
    print(f"Stack: {stack}")


