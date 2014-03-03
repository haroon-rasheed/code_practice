#!/usr/bin/env python


class Node(object):
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class DoubleLinkedList(object):
    def __init__(self):
        self.head = None
        self.tail = None


    def append(self, ele):
        node = self.head
        new_node = Node(ele)


        if self.head is None:
            self.head = new_node

        if self.tail is not None:
            self.tail.next = new_node

        self.tail = new_node

    def showlist(self):
        node = self.head
        i = 0
        while node != None:
            print "Node at position is %s data %s" % (i, node.data)
            node = node.next
            i += 1



if __name__ == '__main__':
    dll = DoubleLinkedList()
    dll.append(1)
    dll.append(2)
    dll.append(3)
    dll.append(4)
    dll.append(5)
    dll.append(6)
    dll.showlist()
