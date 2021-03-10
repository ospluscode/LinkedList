# Singly Linked List implementation
# Create, Insert, Traverse, Search, Delete operations

class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next

    # Insert
    def insertSinglyLL(self, value, location):
        newNode = Node(value)
        if self.head is None:
            self.head = newNode
            self.tail = newNode
        else:
            # Beginning
            if location == 0:
                newNode.next = self.head
                self.head = newNode
            # End
            elif location == 1:
                newNode.next = None
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


    # Traverse
    def traverseSinglyLL(self):
        if self.head is None:
            print("The Singly LL does not exist")
        else:
            node = self.head
            while node is not None:
                print(node.value)
                node = node.next


    # Search
    def searchSinglyLL(self, nodeValue):
        if self.head is None:
           return "The list does not exist"
        else:
            node = self.head
            while node is not None:
                if node.value == nodeValue:
                    return node.value
                node = node.next
            return "The value does not exist"


    #  Delete
    def deleteNode(self, location):
        if self.head is None:
            print("The SinglyLL does not exist")
        else:
            # Beginning
            if location == 0:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    self.head = self.head.next
            # End
            elif location == 1:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    node = self.head
                    while node is not None:
                        if node.next == self.tail:
                            break
                        node = node.next
                    node.next = None
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


    # Delete Entire SinglyLL
    def deleteEntireSinglyLL(self):
        if self.head is None:
            print("The SinglyLL does not exist")
        else:
            self.head = None
            self.tail = None