class ListNode:
    def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
    
    def __str__(self):
        result = []
        current = self
        while current is not None:
            next = current.next
            result.append(str(current.val))
            current = next
        return "->".join(result)

def reverseList(head):
    previous = None
    current = head
    while current is not None:
        next = current.next
        current.next = previous
        previous = current
        current = next
    return previous

def removeNodes(head):
    reversedHead = reverseList(head)
    maxSoFar = -9999999999
    newHead = None
    current = reversedHead
    while current is not None:
        if current.val >= maxSoFar:
            maxSoFar = current.val
            # Create a new node and add it to the front of 'newHead'
            newNode = ListNode(current.val)
            newNode.next = newHead
            newHead = newNode
        current = current.next
    return newHead

head = ListNode(5, ListNode(2, ListNode(13, ListNode(3, ListNode(8)))))
print(removeNodes(head))