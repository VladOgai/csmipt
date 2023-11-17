# binary trees
# 1, 2
class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def is_symmetrical(self):
        if self.left is None and self.right is None:
            return True
        elif self.left is None:
            return False
        elif self.right is None:
            return False
        stack = [(self.left, self.right)]
        while stack:
            x, y = stack.pop()
            if x.value != y.value:
                return False
            if x.left and y.right:
                stack.append((x.left, y.right))
            elif x.left or y.right:
                return False
            if x.right and y.left:
                stack.append((x.right, y.left))
            elif x.right or y.left:
                return False
        return True

    def mirror(self):
        core = Node(self.value, self.right, self.left)
        stack = [(core.left, core.right)]
        while stack:
            x, y = stack.pop()
            if x:
                x = Node(x.value, x.right, x.left)
                stack.append((x.left, x.right))
            if y:
                y = Node(y.value, y.right, y.left)
                stack.append((y.left, y.right))
        return core


xx = Node(1)
xx.left = Node(1)
xx.right = Node(1)
xx.left.left = Node(1)
xx.left.right = Node(2)
xx.right.left = Node(2)
xx.right.right = Node(1)
xx.left.left.left = Node(1)
xx.left.left.right = Node(2)
xx.left.right.left = Node(3)
xx.left.right.right = Node(4)
xx.right.left.left = Node(4)
xx.right.left.right = Node(3)
xx.right.right.left = Node(2)
xx.right.right.right = Node(1)

yy = Node(1)
yy.left = Node(1)
yy.right = Node(2)
yy.left.left = Node(1)
yy.left.right = Node(2)
yy.right.left = Node(3)
yy.right.right = Node(4)
yy.left.left.left = Node(1)
yy.left.left.right = Node(2)
yy.left.right.left = Node(3)
yy.left.right.right = Node(4)
yy.right.left.left = Node(5)
yy.right.left.right = Node(6)
yy.right.right.left = Node(7)
yy.right.right.right = Node(8)

ycore = Node(1)
ycore.left = yy
ycore.right = yy.mirror()

print(xx.is_symmetrical())
print(yy.mirror().left.left.value)
