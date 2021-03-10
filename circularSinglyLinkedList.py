# Circular Singly Linked List implementation
# Create, Insert, Traverse, Search, Delete operations

class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None

class CircularSinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next
            if node == self.tail.next:
                break


    #  Create
    def createCircularSinglyLL(self, nodeValue):
        node = Node(nodeValue)
        node.next = node
        self.head = node
        self.tail = node
        return "The Circular Singly LL created"


    #  Insert
    def insertCircularSinglyLL(self, value, location):
        if self.head is None:
            return "The head reference is None"
        else:
            newNode = Node(value)
            # Beginning
            if location == 0:
                newNode.next = self.head
                self.head = newNode
                self.tail.next = newNode
            # End
            elif location == 1:
                newNode.next = self.tail.next
                self.tail.next = newNode
                self.tail = newNode
            # Middle
            else:
                tempNode = self.head
                index = 0
                while index < location - 1:
                    tempNode = tempNode.next
                    index += 1
                nextNode = tempNode.next
                tempNode.next = newNode
                newNode.next = nextNode
            return "The node inserted"


    # Traverse
    def traverseCircularSinglyLL(self):
        if self.head is None:
            print("The head reference is None")
        else:
            tempNode = self.head
            while tempNode:
                print(tempNode.value)
                tempNode = tempNode.next
                if tempNode == self.tail.next:
                    break


    # Search
    def searchCircularSinglyLL(self, nodeValue):
        if self.head is None:
            return "There is not any node"
        else:
            tempNode = self.head
            while tempNode:
                if tempNode.value == nodeValue:
                    return tempNode.value
                tempNode = tempNode.next
                if tempNode == self.tail.next:
                    return "The node does not exist"


    # Delete
    def deleteNodeInCircularSinglyLL(self, location):
        if self.head is None:
            print("There is not any node")
        else:
            # Beginning
            if location == 0:
                if self.head == self.tail:
                    self.head.next = None
                    self.head = None
                    self.tail = None
                else:
                    self.head = self.head.next
                    self.tail.next = self.head
            # End
            elif location == 1:
                if self.head == self.tail:
                    self.head.next = None
                    self.head = None
                    self.tail = None
                else:
                    node = self.head
                    while node is not None:
                        if node.next == self.tail:
                            break
                        node = node.next
                    node.next = self.head
                    self.tail = node
            # Middle
            else:
                tempNode = self.head
                index = 0
                while index < location - 1:
                    tempNode = tempNode.next
                    index += 1
                nextNode = tempNode.next
                tempNode.next = nextNode.next

    
    # Delete Entire Circular Singly LL
    def deleteEntireCircularSinglyLL(self):
        self.head = None
        self.tail.next = None
        self.tail = None