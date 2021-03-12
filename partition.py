
# Partition a linked list around a value x,
# so all nodes less than x come before all nodes greater than or equal to x

from linkedList import LinkedList

def partition(linked_list, x):
    # create a linked list with 1node, which is the first/head node
    currentNode = linked_list.head
    linked_list.tail = linked_list.head

    # compare first with next and if < x make it first/head node
    while currentNode:
        nextNode = currentNode.next
        currentNode.next = None
        if currentNode.value < x:
            currentNode.next = linked_list.head
            linked_list.head = currentNode
        # if node value is x, make it tail node (of so far list all < x)
        else:
            linked_list.tail.next = currentNode
            linked_list.tail = currentNode
        currentNode = nextNode

    # if all values less than x value, next should be none
    if linked_list.tail.next is not None:
        linked_list.tail.next = None