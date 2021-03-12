
# Two numbers represented by linked lists. Numbers are in reverse order
# Add the numbers and represent the result in reverse, as linked lists
# Add first number take carry , then 2nd then like this continue. (like in math)
# 1->2->3     321
# 4->5->6   + 654
# 5->7->9   = 975

from linkedList import LinkedList

def sumLists(A_llist, B_llist):
    carry_num = 0
    node1 = A_llist.head
    node2 = B_llist.head
    linked_list = LinkedList()

    while node1 or node2:
        result = carry_num
        # take 1st list num
        if node1:
            result += node1.value
            node1 = node1.next
        # take 2nd list num and add
        if node2:
            result += node2.value
            node2 = node2.next
        # add the 1st list and 2nd list sum to a new list
        linked_list.add(int(result % 10))
        carry_num = result / 10
    
    return ll
