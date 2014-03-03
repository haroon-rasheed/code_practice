#!/usr/bin/env python

import copy

class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList(object):
    def __init__(self):
        self.head = None
        self.tail = None


    def showlist(self):
        node = self.head
        i = 1 
        while node != None:
            print "Element at position %s = %s" % (i, node.data)
            i += 1
            node = node.next

    def append(self, node):
        new_node = Node(node)

        if self.head == None:
            self.head = new_node
        
        if self.tail != None:
            self.tail.next = new_node

        self.tail = new_node
            
    
    def delete(self, position):
        node = self.head     
        pass

    def insert_at(self, data, position):
        node = self.head
        new_node = Node(data)

        if position == 0:
            new_node.next = node
            self.head = new_node 
        else:
            i = 1
            while node.next != None and i < position:
                node = node.next
                i += 1
            new_node.next = node.next
            node.next = new_node



    def reverse(self):
        node = self.head     
        reversed_lt = LinkedList()
        while node != None:
            reversed_lt.insert_at(node.data, 0)
            node = node.next
            del node
    
        """
        i = 0 
        while(node.next != None):
            reversed_lt.head = copy.deepcopy(node)
            node = node.next
            #print "Node data =>", node.data
            reversed_lt.tail = copy.deepcopy(reversed_lt.head)
            reversed_lt.head = copy.deepcopy(node)
            reversed_lt.head.next = reversed_lt.tail
            i += 1
            #print "Pos =>", i
            #print "head =>", reversed_lt.head.data
        """   
           
        return reversed_lt

if __name__ == '__main__':
    sll = LinkedList()
    sll.append(1)
    sll.append(2)
    sll.append(3)
    sll.append(4)
    sll.append(5)
    sll.append(6)
    print "original list"
    sll.insert_at(3,3)
    sll.showlist()
    #sll.showlist()
    print "reversed list"
    rsll = sll.reverse()
    rsll.showlist()
