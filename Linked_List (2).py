#<<<<<<< HEAD
class Node:
    def __init__(self, data):
        self.data = data
        self.ref = None


class LinkedList:
    def __init__(self):
        self.head = None

    def traverse(self):
        if self.head is None:
            print("The linked list is empity")
        else:
            n = self.head
            while n is not None:
                print(n.data)
                n = n.ref

    def add_begin(self, data):
        new_node = Node(data)
        new_node.ref = self.head
        self.head = new_node

    def add_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            n = self.head
            while n.ref is not None:
                n = n.ref
            n.ref = new_node

    def add_after(self, data, prev):
        n = self.head
        while n is not None:
            if prev == n.data:
                break
            n = n.ref
        if n is None:
            print("the linked list is empity")
        else:
            new_node = Node(data)
            new_node.ref = n.ref
            n.ref = new_node

    def add_after(self, data, previous):
        n = self.head
        while n is not None:
            if previous == n.data:
                break
            n = n.ref
        if n is None:
            print("the node is absent in the linked lists")
        else:
            new_node = Node(data)
            new_node.ref = n.ref
            n.ref = new_node

    def add_before(self, data, next):
        if self.head is None:
            print("Linked list is emity")
            return
        if self.head.data == next:
            new_node = Node(data)
            new_node.ref = self.head
            self.head = new_node
            return
        n = self.head
        while n.ref is not None:
            if n.ref.data == next:
                break
            n = n.ref
        if n.ref is None:
            print("the node is not found")
        else:
            new_node = Node(data)
            new_node.ref = n.ref
            n.ref = new_node

    def insert_empity(self, data):
        if self.head is None:
            new_node = Node(data)
            self.head = new_node
        else:
            print("Linked list is not empity")

    def delete_begin(self):
        if self.head is None:
            print("the linked list is empity")
        else:
            self.head = self.head.ref

    def delete_end(self):
        if self.head is None:
            print("the linked list is empity.")
        elif self.head.ref is None:
            self.head = None
        else:
            n = self.head
            while n.ref.ref is not None:
                n = n.ref
            n.ref = None

    def delete_by_value(self,value):
        if self.head is None:
            print("The linked list is empity.")
            return
        if value==self.head.data:
            self.head=self.head.ref
            return
        n=self.head
        while n.ref is not None:
            if value==n.ref.data:
                break

            n=n.ref
        if n.ref is None:
            print("The node is absent")
        else:
            n.ref=n.ref.ref

#=======
class Node:
    def __init__(self, data):
        self.data = data
        self.ref = None


class LinkedList:
    def __init__(self):
        self.head = None

    def traverse(self):
        if self.head is None:
            print("The linked list is empity")
        else:
            n = self.head
            while n is not None:
                print(n.data)
                n = n.ref

    def add_begin(self, data):
        new_node = Node(data)
        new_node.ref = self.head
        self.head = new_node

    def add_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            n = self.head
            while n.ref is not None:
                n = n.ref
            n.ref = new_node
    def traverse(self):
        prev=None
        current=self.head
        while current is not None:
            next_node=current.next
            current.next=prev
            prev=current
            current=next_node
        self.head=prev

    def add_after(self, data, prev):
        n = self.head
        while n is not None:
            if prev == n.data:
                break
            n = n.ref
        if n is None:
            print("the linked list is empity")
        else:
            new_node = Node(data)
            new_node.ref = n.ref
            n.ref = new_node

    def add_after(self, data, previous):
        n = self.head
        while n is not None:
            if previous == n.data:
                break
            n = n.ref
        if n is None:
            print("the node is absent in the linked lists")
        else:
            new_node = Node(data)
            new_node.ref = n.ref
            n.ref = new_node

    def add_before(self, data, next):
        if self.head is None:
            print("Linked list is emity")
            return
        if self.head.data == next:
            new_node = Node(data)
            new_node.ref = self.head
            self.head = new_node
            return
        n = self.head
        while n.ref is not None:
            if n.ref.data == next:
                break
            n = n.ref
        if n.ref is None:
            print("the node is not found")
        else:
            new_node = Node(data)
            new_node.ref = n.ref
            n.ref = new_node

    def insert_empity(self, data):
        if self.head is None:
            new_node = Node(data)
            self.head = new_node
        else:
            print("Linked list is not empity")

    def delete_begin(self):
        if self.head is None:
            print("the linked list is empity")
        else:
            self.head = self.head.ref

    def delete_end(self):
        if self.head is None:
            print("the linked list is empity.")
        elif self.head.ref is None:
            self.head = None
        else:
            n = self.head
            while n.ref.ref is not None:
                n = n.ref
            n.ref = None

    def delete_by_value(self,value):
        if self.head is None:
            print("The linked list is empity.")
            return
        if value==self.head.data:
            self.head=self.head.ref
            return
        n=self.head
        while n.ref is not None:
            if value==n.ref.data:
                break

            n=n.ref
        if n.ref is None:
            print("The node is absent")
        else:
            n.ref=n.ref.ref

#>>>>>>> c5c997cd7e2a8429e9c67f395d1859a11859a00c
