class Solution:
    def removeNodes(head):
        if not head:
            return None
        # Recursively process the rest of the list
        new_head = self.removeNodes(head.next)
        # Connect the current node to the result of the recursive call
        head.next = new_head
        # Determine if the current node should be kept
        if not new_head or head.val >= new_head.val:
            return head  # Keep the current node
        return new_head # Skip the current node
                