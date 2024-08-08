# Runtime: 43 ms
# Memory Usage: 18.5 MB

class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        idx = 1
        current_node = head
        even_node_head = None
        previous_odd_node = None
        previous_even_node = None
        
        while current_node:
            if idx % 2 == 0:
                previous_odd_node.next = current_node.next
                if not even_node_head:
                    even_node_head = ListNode(val=current_node.val)
                    previous_even_node = even_node_head
                else:
                    previous_even_node.next = ListNode(val=current_node.val)
                    previous_even_node = previous_even_node.next
            else:
                previous_odd_node = current_node
            
            current_node = current_node.next
            idx += 1
        
        if even_node_head:
            previous_odd_node.next = even_node_head
        
        return head
        
