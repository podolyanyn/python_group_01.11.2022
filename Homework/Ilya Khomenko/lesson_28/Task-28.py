#Task-1
class Node:

  def __init__(self, initdata):
    self.data = initdata
    self.next = None
  

  def getData(self):
    return self.data
    

  def getNext(self):
    return self.next
    

  def setData(self, newdata):
    self.data = newdata
    

  def setNext(self, newnext):
    self.next = newnext
    
class UnorderedList:

  def __init__(self):
    self.head = None
    self.llist= []
  

  def isEmpty(self):
    return self.head == None
 

  def add(self, item):
    temp = Node(item)
    temp.setNext(self.head)
    self.head = temp
    self.llist.append(self.head.data)
   

  def size(self):
    current = self.head
    count = 0
    while current != None:
      count += 1
      current = current.getNext()
      
    return count
    

  def index(self, item):
    current = self.head
    found = False
    index = 0
    
    while current != None and not found:
      if current.getData() != item:
        index +=1
        current = current.getNext()
      else:
        found = True
    if found:
      return index
    else:
      return "Not Found"


  
  def pop(self):
    current = self.head
    previous = None
    
    if current == None:
      return "No item in list"
    
    while current.getNext() != None:
      previous = current
      current = current.getNext()
    
    previous.setNext(None)
    return current.getData()

  def list_slice(self,start,stop):
    print(self.llist[slice(start,stop)])
    

      



def main():
  linkedlist = UnorderedList()
  linkedlist.add(1)
  linkedlist.add(2)
  linkedlist.add(3)
  linkedlist.add(4)
  linkedlist.add(5)
  linkedlist.add(6)
  linkedlist.add(7)
  linkedlist.list_slice(0,5)

main()



#Task-2
# class Node:
#     def __init__(self,data) -> None:
#         self.data = data
#         self.next = None




# class Stack:
#     def __init__(self) -> None:
#         self.head = None

#     def isEmpty(self):
#         return self.head == None

#     def push(self,data):
#         if self.head == None:
#             self.head = Node(data)

#         else:
#             newnode = Node(data)
#             newnode.next = self.head
#             self.head = newnode

#     def pop(self):
#         if self.isEmpty():
#             return None
#         else:
#             p_node = self.head
#             self.head = self.head.next
#             p_node.next = None
#             return p_node.data

#     def peek(self):
#         if self.isEmpty():
#             return None
#         else:
#             return self.head.data



#Task-3
# class Node:
#     def __init__(self,data) -> None:
#         self.data = data
#         self.next = None


# class Queue:
#     def __init__(self) -> None:
#         self.front = None
#         self.rear = None

#     def isEmpty(self):
#         return self.front == None

#     def EnQueue(self,item):
#         if self.rear is None:
#             self.front = Node(item)
#             self.rear = self.front

#     def DeQueue(self):
#         if self.isEmpty():
#             return None
#         else:
#             t = self.front.data
#             self.front = self.front.next
#             return t



# q = Queue()
# print(q.EnQueue(10))
# print(q.EnQueue(20))
# print(q.DeQueue())
# print(q.DeQueue())
# print(q.EnQueue(30))
# print(q.EnQueue(40))
# print(q.EnQueue(50))
# print(q.DeQueue())

