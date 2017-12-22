class Node:
    def __init__(self, key, NIL = "NIL"):
        self.key = key
        self.left = NIL
        self.right = NIL
        self.p = NIL

    def getKey(self):
        return self.key

    def setKey(self, key):
        self.key = key

    def getChildren(self):
        children = []
        if self.left is not "NIL":
            children.append(self.left)
        if self.right is not "NIL":
            children.append(self.right)
        return children


class ABR:
    def __init__(self):
        self.NIL = "NIL"  # In un Albero Binario si considera NIL come lo stato di un nodo libero
        self.root = Node("NIL")

    def setRoot(self, key):
        self.root = Node(key)

    def insert(self, key):
        z = Node(key, self.NIL)
        if self.root.key is self.NIL:
            self.root = z
        else:
            self.insertNode(self.root, z)

    def insertNode(self, current_node, z):
        if z.key <= current_node.key:
            if current_node.left is not self.NIL:
                self.insertNode(current_node.left, z)
            else:
                current_node.left = z
                z.p = current_node
                return z
        elif z.key > current_node.key:
            if current_node.right is not self.NIL:
                self.insertNode(current_node.right, z)
            else:
                current_node.right = z
                z.p = current_node
                return z

    def find(self, key):
        return self.findNode(self.root, key)

    def findNode(self, currentNode, key):
        if currentNode is self.NIL:
            return False
        elif currentNode.key == key:
            return True
        elif key < currentNode.key:
            self.findNode(currentNode.left, key)
        else:
            self.findNode(currentNode.right, key)

    def inorder(self):
        def _inorder(v):
            if v is self.NIL:
                return
            if v.left is not self.NIL:
                _inorder(v.left)
            print v.key
            if v.right is not self.NIL:
                _inorder(v.right)
        _inorder(self.root)

    def transplant(self, u, v):
        if u.p == self.NIL:
            self.root = v
        elif u == u.p.left:
            u.p.left = v
        else:
            u.p.right = v
        if v != self.NIL:
            v.p = u.p

    def deleteNode(self, z):
        if z.left == self.NIL:
            self.transplant(z, z.right)
        elif z.right == self.NIL:
            self.transplant(z, z.left)
        else:
            y = self.treeMinimum(z.right)
            if y.p != z:
                self.transplant(y, y.right)
                y.right = z.right
                y.right.p = y
            self.transplant(z, y)
            y.left = z.left
            y.left.p = y

    def treeMinimum(self, x):
        while x.left != self.NIL:
            x = x.left
        return x

    def treeMaximum(self, x):
        while x.right != self.NIL:
            x = x.right
        return x

    def getHeight(self, x):
        if x == self.NIL:
            return -1
        else:
            return max(self.getHeight(x.left), self.getHeight(x.right)) + 1
