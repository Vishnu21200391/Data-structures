class Node:
    def __init__(self, item=None, next=None):
        self.item = item
        self.next = next

class SLL:
    def __init__(self):
        self.start = None

    def isempty(self):
        return self.start is None

    def search(self, data):
        temp = self.start
        while temp:
            if temp.item == data:
                return temp
            temp = temp.next
        return None  # Explicitly return None if not found

    def insert_at_begin(self, data):
        new_node = Node(data, self.start)
        self.start = new_node

    def insert_at_after(self, data, node):
        if node is None:
            return
        new_node = Node(data, node.next)
        node.next = new_node

    def insert_at_last(self, data):
        new_node = Node(data)
        if self.isempty():
            self.start = new_node
            return
        temp = self.start
        while temp.next:
            temp = temp.next
        temp.next = new_node

    def print_all(self):
        temp = self.start
        while temp:
            print(temp.item, end=" ")
            temp = temp.next
        print()

    def delete_at_begin(self):
        if not self.isempty():
            self.start = self.start.next

    def delete_item(self, data):
        if self.isempty():
            return
        if self.start.item == data:
            self.start = self.start.next
            return
        temp = self.start
        while temp.next:
            if temp.next.item == data:
                temp.next = temp.next.next
                return
            temp = temp.next

    def delete_last(self):
        if self.isempty():
            return
        if self.start.next is None:  # Only one element
            self.start = None
            return
        temp = self.start
        while temp.next.next:
            temp = temp.next
        temp.next = None

    def __iter__(self):
        return SLLIterator(self.start)

class SLLIterator:
    def __init__(self, start):
        self.current = start

    def __iter__(self):
        return self

    def __next__(self):
        if not self.current:
            raise StopIteration
        data = self.current.item
        self.current = self.current.next
        return data

# Testing the corrected SLL
myList = SLL()
print(myList.isempty())  # True
myList.insert_at_begin(45)
myList.insert_at_begin(100)
myList.insert_at_begin(50)
myList.insert_at_after(78, myList.search(45))
myList.insert_at_last(199)
myList.print_all()  # Output: 50 100 45 78 199

for i in myList:
    print(i, end="-")
print()