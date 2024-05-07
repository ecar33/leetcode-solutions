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

def doubleIt(head):
        dummy = ListNode()
        current = dummy
        carry = 0
        head = reverseList(head)
        l1 = head
        l2 = head
        
        while l1 or l2 or carry:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0
            total = v1 + v2 + carry
            
            carry = total // 10
            current.next = ListNode(total % 10)
            current = current.next
            
            if l1:
                l1 = l1.next
            
            if l2:
                l2 = l2.next
        
        dummy.next = reverseList(dummy.next)
        return dummy.next

head = ListNode(1, ListNode(8, ListNode(9)))
print(doubleIt(head))