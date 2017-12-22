from BinaryTree import ABR
from BinaryTree import Node
RED = True
BLACK = False


class RBNode(Node):
    def __init__(self, key, NIL):
        Node.__init__(self, key, NIL)
        self.color = BLACK

    def getColor(self):
        return self.color

    def setColor(self, color):
        self.color = color


class ARN(ABR):
    def __init__(self):
        ABR.__init__(self)
        self.NIL = RBNode("NIL", self.NIL) # In un Albero rosso-nero NIL e' un vero e proprio nodo sentinella
        self.root = self.NIL
        self.root.p = self.NIL

    def RBInsert(self, key):
        z = RBNode(key, self.NIL)
        z.p = self.NIL
        if self.root is self.NIL:
            self.root = z
        else:
            self.insertNode(self.root, z)
            z.color = RED
        self.RBInsert_fixup(z)

    def RBInsert_fixup(self, z):
        while z.p.color == RED:
            if z.p == z.p.p.left:
                y = z.p.p.right
                if y.color == RED:
                    z.p.color = BLACK
                    y.color = BLACK
                    z.p.p.color = RED
                    z = z.p.p
                else:
                    if z == z.p.right:
                        z = z.p
                        self.left_rotate(z)
                    z.p.color = BLACK
                    z.p.p.color = RED
                    self.right_rotate(z.p.p)
            else:
                if z.p == z.p.p.right:
                    y = z.p.p.left
                    if y.color == RED:
                        z.p.color = BLACK
                        y.color = BLACK
                        z.p.p.color = RED
                        z = z.p.p
                    else:
                        if z == z.p.left:
                            z = z.p
                            self.right_rotate(z)
                        z.p.color = BLACK
                        z.p.p.color = RED
                        self.left_rotate(z.p.p)
        self.root.color = BLACK

    def left_rotate(self, x):
        y = x.right
        x.right = y.left
        if y.left != self.NIL:
            y.left.p = x
        y.p = x.p
        if x.p == self.NIL:
            self.root = y
        elif x == x.p.left:
            x.p.left = y
        else:
            x.p.right = y
        y.left = x
        x.p = y

    def right_rotate(self, x):
        y = x.left
        x.left = y.right
        if y.right is not self.NIL:
            y.right.p = x
        y.p = x.p
        if x.p == self.NIL:
            self.root = y
        elif x == x.p.right:
            x.p.right = y
        else:
            x.p.left = y
        y.right = x
        x.p = y
