# Return nth element from the last node

from linkedList import LinkedList

def nthToLast(linked_list, n):
    # pointer to reach nth node
    pointer1 = linked_list.head
    # pointer to reach last node
    pointer2 = linked_list.head

    # place pointers n node from each other
    for i in range(n):
        if pointer2 is None:
            return None
        pointer2 = pointer2.next

    # move pointer until pointer2 reach to end
    while pointer2:
        pointer1 = pointer1.next
        pointer2 = pointer2.next
    return pointer1