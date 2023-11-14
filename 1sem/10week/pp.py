# h6
class Node:
    def __init__(self, val):
        self.val = val
        self.parent = None
        self.c1 = None
        self.c2 = None


class Heap:
    def __init__(self):
        self.root = None

    def print_heap(self, n=None):
        pass

    def max_to_min(self):



kucha = Heap()
root = Node(200)

c1 = Node(190)
c1.parent = root
c2 = Node(180)
c2.parent = root
root.c1 = c1
root.c2 = c2

c11 = Node(170)
c11.parent = c1
c12 = Node(160)
c12.parent = c1
c1.c1 = c11
c1.c2 = c12

c21 = Node(150)
c21.parent = c2
c22 = Node(140)
c22.parent = c2
c2.c1 = c21
c2.c2 = c22

c111 = Node(130)
c111.parent = c11
c112 = Node(120)
c112.parent = c11
c11.c1 = c111
c11.c2 = c112

c121 = Node(110)
c121.parent = c12
c122 = Node(100)
c122.parent = c12
c12.c1 = c121
c12.c2 = c122

c211 = Node(90)
c211.parent = c21
c212 = Node(80)
c212.parent = c21
c21.c1 = c211
c21.c2 = c212

c221 = Node(70)
c221.parent = c22
c222 = Node(60)
c222.parent = c22
c22.c1 = c221
c22.c2 = c222

kucha.root = root

kucha.print_heap()
kucha.max_to_min()
kucha.print_heap()

import heapq