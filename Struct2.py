# добавляется в среднем за O(log(n)) в худшем случае за O(n)
# получается элемент, удаляется и изменяется за O(log(n))

import random

class Node:
    def __init__(self, key, weight):
        self.key = key
        self.weight = weight
        self.total_weight = weight  
        self.color = 1
        self.left = None
        self.right = None
        self.parent = None

class RedBlackTree:
    def __init__(self):
        self.TNULL = Node(0, 0)
        self.TNULL.color = 0
        self.TNULL.total_weight = 0
        self.TNULL.left = None
        self.TNULL.right = None
        self.root = self.TNULL


    def update_total_weight(self, node):
        if node:
            node.total_weight = (
                node.weight
                + (node.left.total_weight if node.left else 0)
                + (node.right.total_weight if node.right else 0)
            )

    def left_rotate(self, x):
        y = x.right
        x.right = y.left
        if y.left != self.TNULL:
            y.left.parent = x
        y.parent = x.parent
        if x.parent is None:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y
        self.update_total_weight(x)  
        self.update_total_weight(y)

    def right_rotate(self, x):
        y = x.left
        x.left = y.right
        if y.right != self.TNULL:
            y.right.parent = x
        y.parent = x.parent
        if x.parent is None:
            self.root = y
        elif x == x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y
        y.right = x
        x.parent = y
        self.update_total_weight(x)  
        self.update_total_weight(y)

    def insert_fix(self, k):
        while k.parent.color == 1:
            if k.parent == k.parent.parent.right:
                u = k.parent.parent.left
                if u.color == 1:
                    u.color = 0
                    k.parent.color = 0
                    k.parent.parent.color = 1
                    k = k.parent.parent
                else:
                    if k == k.parent.left:
                        k = k.parent
                        self.right_rotate(k)
                    k.parent.color = 0
                    k.parent.parent.color = 1
                    self.left_rotate(k.parent.parent)
            else:
                u = k.parent.parent.right
                if u.color == 1:
                    u.color = 0
                    k.parent.color = 0
                    k.parent.parent.color = 1
                    k = k.parent.parent
                else:
                    if k == k.parent.right:
                        k = k.parent
                        self.left_rotate(k)
                    k.parent.color = 0
                    k.parent.parent.color = 1
                    self.right_rotate(k.parent.parent)
            if k == self.root:
                break
        self.root.color = 0

    def add(self, key, weight):
        node = Node(key, weight)
        node.parent = None
        node.left = self.TNULL
        node.right = self.TNULL
        node.color = 1

        y = None
        x = self.root

        while x != self.TNULL:
            y = x
            if node.key < x.key:
                x = x.left
            elif node.key == x.key:
                x.weight = weight  
                self.update_total_weight(x)
                return
            else:
                x = x.right

        node.parent = y
        if y is None:
            self.root = node
        elif node.key < y.key:
            y.left = node
        else:
            y.right = node
        current = node
        while current.parent:
            self.update_total_weight(current)
            current = current.parent
        else:
            self.update_total_weight(current)
        if node.parent is None:
            node.color = 0
            return

        if node.parent.parent is None:
            return

        self.insert_fix(node)

    def delete(self, key):
        self.delete_node_helper(self.root, key)

    def delete_node_helper(self, node, key):
        z = self.TNULL
        while node != self.TNULL:
            if node.key == key:
                z = node
            if node.key <= key:
                node = node.right
            else:
                node = node.left

        if z == self.TNULL:
            return

        y = z
        y_original_color = y.color
        if z.left == self.TNULL:
            x = z.right
            self.rb_transplant(z, z.right)
        elif z.right == self.TNULL:
            x = z.left
            self.rb_transplant(z, z.left)
        else:
            y = self.minimum(z.right)
            y_original_color = y.color
            x = y.right
            if y.parent == z:
                x.parent = y
            else:
                self.rb_transplant(y, y.right)
                y.right = z.right
                y.right.parent = y

            self.rb_transplant(z, y)
            y.left = z.left
            y.left.parent = y
            y.color = z.color
            self.update_total_weight(y)

        current = x.parent
        while current:
            self.update_total_weight(current)
            current = current.parent

        if y_original_color == 0:
            self.delete_fix(x)

    
    def rb_transplant(self, u, v):
        if u.parent == None:
            self.root = v
        elif u == u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v
        v.parent = u.parent

    def delete_fix(self, x):
        while x != self.root and x.color == 0:
            if x == x.parent.left:
                s = x.parent.right
                if s.color == 1:
                    s.color = 0
                    x.parent.color = 1
                    self.left_rotate(x.parent)
                    s = x.parent.right
                if s.left.color == 0 and s.right.color == 0:
                    s.color = 1
                    x = x.parent
                else:
                    if s.right.color == 0:
                        s.left.color = 0
                        s.color = 1
                        self.right_rotate(s)
                        s = x.parent.right
                    s.color = x.parent.color
                    x.parent.color = 0
                    s.right.color = 0
                    self.left_rotate(x.parent)
                    x = self.root
            else:
                s = x.parent.left
                if s.color == 1:
                    s.color = 0
                    x.parent.color = 1
                    self.right_rotate(x.parent)
                    s = x.parent.left
                if s.right.color == 0 and s.left.color == 0:
                    s.color = 1
                    x = x.parent
                else:
                    if s.left.color == 0:
                        s.right.color = 0
                        s.color = 1
                        self.left_rotate(s)
                        s = x.parent.left
                    s.color = x.parent.color
                    x.parent.color = 0
                    s.left.color = 0
                    self.right_rotate(x.parent)
                    x = self.root
        x.color = 0


    def get(self):
        if self.root.total_weight == 0:
            return None
        threshold = random.uniform(0, self.root.total_weight)
        current = self.root
        while current != self.TNULL:
            left_weight = current.left.total_weight if current.left != self.TNULL else 0
            if threshold < left_weight:
                current = current.left
            elif threshold < left_weight + current.weight:
                return current.key
            else:
                threshold -= (left_weight + current.weight)
                current = current.right
        return None

    
    def minimum(self, node):
        while node.left != self.TNULL:
            node = node.left
        return node
    

