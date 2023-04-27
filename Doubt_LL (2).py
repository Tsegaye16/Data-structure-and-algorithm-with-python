class Node:
    def __init__(self, data):
        self.data = data
        self.nex_ref = None
        self.prev_ref = None


class Doubly_Linked_List:
    def __init__(self):
        self.head = None

    def print_DLL_Forward(self):
        print()
        if self.head is None:
            print("linked list is empty")
        else:
            n = self.head
            while n is not None:
                print(n.data, "-->", end=" ")
                n = n.nex_ref

    def print_DDL_backward(self):
        if self.head is None:
            print("The linked list is empty")
        else:
            n = self.head
            while n.nex_ref is not None:
                n = n.nex_ref
            while n is not None:
                print(n.data, "-->", end=" ")
                n = n.prev_ref

    def insert_To_empty(self, data):
        if self.head is None:
            new_node = Node(data)
            self.head = new_node
        else:
            print("Linked list is not empty")

    def add_To_begin(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.nex_ref = self.head
            self.head.prev_ref = new_node
            self.head = new_node
            new_node = Node(data)

    def add_To_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            n = self.head
            while n.nex_ref is not None:
                n = n.nex_ref
            n.nex_ref = new_node
            new_node.prev_ref = n

    def Add_After(self, data, prev):
        if self.head is None:
            print("Linked list is empty.")
        else:
            n = self.head
            while n is not None:
                if prev == n.data:
                    break
                n = n.nex_ref
            if n is None:
                print("the node is absent in the linked list")
            else:
                new_node = Node(data)
                new_node.nex_ref = n.nex_ref
                new_node.prev_ref = n
                if n.nex_ref is not None:
                    n.nex_ref.prev_ref = new_node
                n.nex_ref = new_node

    def Add_before(self, data, next):
        if self.head is None:
            print("Linked list is empty.")
        else:
            n = self.head
            while n is not None:
                if next == n.data:
                    break
                n = n.nex_ref
            if n is None:
                print("The given node is absent in the linked list")
            else:
                new_node = Node(data)
                new_node.nex_ref = n
                new_node.prev_ref = n.prev_ref
                if n.prev_ref is not None:
                    n.prev_ref.nex_ref = new_node
                else:
                    self.head = new_node
                n.prev_ref = new_node

    def delete_begin(self):
        if self.head is None:
            print("Linked list is empty")
            return
        if self.head.nex_ref is None:
            self.head = None
        else:
            self.head = self.head.nex_ref
            self.head.prev_ref = None

    def delete_end(self):
        if self.head is None:
            print("The linked list is empty")
            return
        if self.head.nex_ref is None:
            self.head = None
        else:
            n = self.head
            while n.nex_ref is not None:
                n = n.nex_ref
            n.prev_ref.nex_ref = None

    def delete_By_value(self, value):
        if self.head is None:
            print("The linked list is empty")
            return
        if self.head.nex_ref is None:
            if value == self.head.data:
                self.head = None
            else:
                print("The value is not present")
            return
        if self.head.data == value:
            self.head = self.head.nex_ref
            self.head.prev_ref = None
            return
        n = self.head
        while n.nex_ref is not None:
            if value == n.data:
                break
            n = n.nex_ref
        if n.nex_ref is not None:
            n.nex_ref.prev_ref = n.prev_ref
            n.prev_ref.nex_ref = n.nex_ref
        else:
            if n.data == value:
                n.prev_ref.nex_ref = None
            else:
                print("The value is empty")
