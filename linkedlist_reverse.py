class Node:
    def __init__(self, newData):
        self.data = newData
        self.next = None

def reverseList(head):
    # Initialize three pointers: curr, prev and next
    curr = head
    prev = None
    # Traverse all the nodes of Linked List
    while curr is not None:
        # Store next
        nextNode = curr.next
        # Reverse current node's next pointer
        curr.next = prev
        # Move pointers one position ahead
        prev = curr
        curr = nextNode
    # Return the head of reversed linked list
    return prev