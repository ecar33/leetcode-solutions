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
    

head = ListNode(5, ListNode(2, ListNode(13, ListNode(3, ListNode(8)))))
print(reverseList(head))