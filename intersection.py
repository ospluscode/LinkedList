
# Determine if two lists intersect. Return the intersecting node
# Intersection is determined based on reference.
# Up to the intersection node the lists are different after they become one

from linkedList import LinkedList, Node

def intersection(A_llist, B_llist):
    # Linked Lists are not intersecting
    if A_llist.tail is not B_llist.tail:
        return False

    # find the lengths of lists
    lenA, lenB = len(A_llist), len(B_llist)

    # find which is short and which is long
    short = A_llist if lenA < lenB else B_llist
    long = B_llist if lenA < lenB else A_llist

    # find diff between 2 lists
    diff = len(long) - len(short)
    longNode = long.head
    shortNode = short.head

    # bring long lists node to short lists first node
    for i in range(diff):
        longNode = longNode.next

    # Find when both short and long nodes point to the same node (Intersecting)
    while shortNode is not longNode:
        shortNode = shortNode.next
        longNode = longNode.next
    
    return longNode