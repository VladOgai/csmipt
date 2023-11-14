class Node:
    def __init__(self, data):
        self.item = data
        self.nref = None
        self.pref = None


class DoublyLinkedList:
    def __init__(self):
        self.start_node = None

    def insert_in_emptylist(self, data):
        if self.start_node is None:
            new_node = Node(data)
            self.start_node = new_node
        else:
            print('list is not empty')

    def insert_at_start(self, data):
        if self.start_node is None:
            new_node = Node(data)
            self.start_node = new_node
            print('node inserted')
        else:
            new_node = Node(data)
            new_node.nref = self.start_node
            self.start_node.pref = new_node
            self.start_node = new_node

    def insert_at_end(self, data):
        if self.start_node is None:
            new_node = Node(data)
            self.start_node = new_node
        else:
            new_node = Node(data)
            n = self.start_node
            while n.nref is not None:
                n = n.nref
            new_node.pref = n
            n.nref = new_node

    def insert_after_item(self, x, data):
        if self.start_node is None:
            print('list is empty')
        else:
            n = self.start_node
            while n is not None:
                if n.item == x:
                    break
                n = n.nref
            if n is None:
                print('item not in list')
            else:
                new_node = Node(data)
                new_node.pref = n
                new_node.nref = n.nref
                if n.nref is not None:
                    n.nref.pref = new_node
                n.nref = new_node

    def insert_before_item(self, x, data):
        if self.start_node is None:
            print('list is empty')
        else:
            n = self.start_node
            while n is not None:
                if n.item == x:
                    break
                n = n.nref
            if n is None:
                print('item not in list')
            else:
                new_node = Node(data)
                new_node.nref = n
                new_node.pref = n.pref
                if n.pref is not None:
                    n.pref.nref = new_node
                n.pref = new_node

    def traverse_list(self):
        if self.start_node is None:
            print("List has no element")
        else:
            n = self.start_node
            while n is not None:
                print(n.item, " ")
                n = n.nref

    def delete_at_start(self):
        if self.start_node is None:
            print("The list has no element to delete")
        elif self.start_node.nref is None:
            self.start_node = None
        else:
            self.start_node = self.start_node.nref
            self.start_node.pref = None

    def delete_at_end(self):
        if self.start_node is None:
            print('The list has no elements to delete')
        elif self.start_node.nref is None:
            self.start_node = None
        else:
            n = self.start_node
            while n.nref is not None:
                n = n.nref
            n.pref.nref = None

    def delete_element_by_value(self, x):
        # check empty list
        if self.start_node is None:
            print("The list has no element to delete")
            return
            # check if list is a single element
        if self.start_node.nref is None:
            if self.start_node.item == x:
                self.start_node = None
            else:
                print("Item not found")
                return
                # list has > 1 element, and desirable elem is the first in the list
        # folllowing the delete_at_start() method
        if self.start_node.item == x:
            self.start_node = self.start_node.nref
            self.start_node.pref = None
            return
            # list is nonsingle-element and desirable elem is not the first
        n = self.start_node
        while n.nref is not None:
            if n.item == x:
                break
            n = n.nref
        if n.nref is not None:
            n.pref.nref = n.nref
            n.nref.pref = n.pref
        else:
            if n.item == x:
                n.pref.nref = None
            else:
                print("Element not found")

    def reverse_linked_list(self):
        if self.start_node is None:
            print("The list has no element to delete")
            return
        p = self.start_node
        q = p.nref
        p.nref = None
        p.pref = q
        while q is not None:
            q.pref = q.nref
            q.nref = p
            p = q
            q = q.pref
        self.start_node = p
