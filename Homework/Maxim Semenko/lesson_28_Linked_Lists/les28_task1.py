class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next

    def set_next(self, new_next):
        self.next = new_next

class UnorderedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def is_empty(self):
        return self.head is None

    def add(self, item):
        temp = Node(item)
        temp.set_next(self.head)
        self.head = temp
        if self.tail is None:
            self.tail = temp
        self.length += 1

    def size(self):
        return self.length

    def search(self, item):
        current = self.head
        found = False
        while current is not None and not found:
            if current.get_data() == item:
                found = True
            else:
                current = current.get_next()
        return found

    def remove(self,item):
        current = self.head
        previous = None
        found = False
        while current is not None and not found:
            if current.get_data() == item:
                found = True
            else:
                previous = current
                current = current.get_next()
        if previous is None:
            self.head = current.get_next()
        else:
            if current.get_next() is None:
                self.tail = previous
            previous.set_next(current.get_next())
        self.length -= 1

    def display(self):
        current = self.head
        string = '['
        while current is not None:
            string += str(current.get_data())
            if current.get_next() is not None:
                string += ', '
            current = current.get_next()
        string += ']'
        return string

    def append(self, item):
        new_node = Node(item)
        last = self.tail
        if last:
            last.set_next(new_node)
        else:
            self.head = new_node
        self.tail = new_node
        self.length += 1

    def insert(self, index, item):
        new_node = Node(item)
        current = self.head
        previous = None
        count = 0
        found = False
        if index > self.length-1:
            raise IndexError('List Index Out Of Range')
        while current is not None and not found:
            if count == index:
                found = True
            else:
                previous = current
                current = current.get_next()
                count += 1
        if previous is None:
            new_node.set_next(self.head)
            self.head = new_node
        else:
            new_node.set_next(current)
            previous.set_next(new_node)
        self.length += 1

    def index(self, item):
        pos = 0
        current = self.head
        found = False
        while current is not None and not found:
            if current.get_data() == item:
                found = True
            else:
                current = current.get_next()
                pos += 1
        if not found:
            raise ValueError('Value not present in the List')
        return pos

    def pop(self, index=None):
        if index is None:
            index = self.length-1
        if index > self.length-1:
            raise IndexError('List Index Out Of Range')
        current = self.head
        previous = None
        found = False
        if current:
            count = 0
            while current.get_next() is not None and not found:
                if count == index:
                    found = True
                else:
                    previous = current
                    current = current.get_next()
                    count += 1
            if previous is None:
                self.head = current.get_next()
                if current.get_next() is None:
                    self.tail = current.get_next()
            else:
                self.tail = previous
                previous.set_next(current.get_next())
        self.length -= 1
        return current.get_data()

if __name__ == "__main__":
    my_list = UnorderedList()
    my_list.add("a")
    my_list.add("b")
    my_list.add("c")
    my_list.append("d")
    print(my_list.display())
    my_list.pop(1)
    print(my_list.display())
    my_list.insert(1, "e")
    print(my_list.display())
    print(my_list.index("e"))
    my_list.remove('a')
    print(my_list.display())
    print(my_list.search('d'))
    print(my_list.search('f'))