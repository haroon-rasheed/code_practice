#!/usr/bin/env python

#from __future__ import print_function


class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

    def __str__(self):
        return str(self.data)

class LinkedList(object):
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, data):
        new_node = Node(data)

        if self.head == None:
            self.head = new_node
        if self.tail != None:
            self.tail.next = new_node

        self.tail = new_node
        #self.showlist()


    def delat(self, position):
        node = self.head
        if position == 0:
            self.head = self.head.next
        else:
            i = 0
            while ( node != None and i < position):
                prev = node
                node = node.next
                i += 1

            prev.next = node.next
            del(node)
            print "After deleting element at position = %s" % (position)
            self.showlist()

    def insertat(self, position, data):
        print "After inserting element %s at position %s" % (data, position)
        new_node = Node(data)
        node = self.head

        if position == 0:
            self.head = new_node
            new_node.next = node
        else:
            i = 0
            while ( node != None and i < position):
                prev = node
                node = node.next
                i += 1

            prev.next = new_node
            new_node.next = node


    def showlist(self):
        node = self.head
        i = 0
        while node != None:
            print "Element at position %s = %s" % (i, node)
            i += 1
            node = node.next

if __name__ == '__main__':
    sll = LinkedList()
    sll.append(1)
    sll.append(2)
    sll.append(3)
    sll.append(4)
    sll.append(5)
    sll.append(6)
    sll.showlist()
    sll.delat(4)
    sll.insertat(2, 3)
    sll.showlist()
    sll.insertat(0, 9)
    sll.showlist()
