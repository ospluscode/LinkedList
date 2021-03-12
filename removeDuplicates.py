# Remove duplicates from an unsorted linked list
# Make sure to write the algorithms before implementation

# this class exist in the repo
from linkedList import LinkedList

# O(n) and O(n) solution with temp buffer
def removeDuplicates(linked_list):
    if linked_list.head is None:
        return
    else:
        currentNode = linked_list.head
        # using temporary buffer to store values
        visited = set([currentNode.value])
        while currentNode.next:
            if currentNode.next.value in visited:
                currentNode.next = currentNode.next.next
            else:
                visited.add(currentNode.next.value)
                currentNode = currentNode.next
        return linked_list


# O(n*n) and O(1) solution without temp buffer
def removeDuplicates2(linked_list):
    if linked_list.head is None:
        return
    
    currentNode = linked_list.head
    while currentNode:
        runner = currentNode
        while runner.next:
            if runner.next.value == currentNode.value:
                runner.next = runner.next.next
            else:
                runner = runner.next
        currentNode = currentNode.next
    return linked_list.head