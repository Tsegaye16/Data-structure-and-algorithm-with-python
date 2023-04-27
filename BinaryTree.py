class BST:
    def __init__(self, root):
        self.root = root
        self.right = None
        self.left = None

    def insert(self, data):
        if self.root is None:
            self.root = data
            return
        if self.root > data:
            if self.left:
                self.left.insert(data)
            else:
                self.left = BST(data)
        else:
            if self.right:
                self.right.insert(data)
            else:
                self.right = BST(data)

    def search(self, data):
        if self.root == data:
            print("The data is present in the tree")
            return
        if self.root > data:
            if self.left:
                self.left.search(data)
            else:
                print("The data is not present in the tree")
        else:
            if self.right:
                self.right.search(data)
            else:
                print("The data is not present in the tree")

    def pre_order(self):
        print(self.root, end=" ")
        if self.left:
            self.left.pre_order()
        if self.right:
            self.right.pre_order()

    def in_order(self):
        if self.left:
            self.left.in_order(self)
        print(self.root)
        if self.right():
            self.right.in_rder(self)

    def post_order(self):
        if self.left:
            self.left.post_order(self)
        if self.right:
            self.right.post_order(self)
        print(self.root)

    def delete(self, data):
        if self.root is None:
            print("The tree is empty")
            return
        if data < self.root:
            if self.left:
                self.left = self.left.delete(data)
            else:
                print("the given onde is not present")
        elif data > self.root:
            if self.right:
                self.right = self.right.delete(data)
            else:
                print("the given onde is not present")
        else:
            if self.left is None:
                temp = self.right
                self = None
                return temp
            if self.right is None:
                temp = self.left
                self = None
                return temp
            node = self.right
            while node.left:
                node = node.left
            self.root = node.root
            self.right = self.right.delete(node.root)
        return self


method = BST(10)
n = int(input("enter the number of none you went"))

for i in range(n):
    k = int(input())
    method.insert(k)
print("pre-order")
method.pre_order()
print("searching")
# method.search(7)
method.delete(7)
method.pre_order()
