# Runtime: 51 ms
# Memory Usage: 16.6 MB

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        round_val = 0
        l1_cursor = l1
        l2_cursor = l2
        root = None
        
        round_val, val = divmod(l1_cursor.val + l2_cursor.val + round_val, 10)
        root = ListNode(val, None)
        root_cursor = root
        
        while l1_cursor.next or l2_cursor.next or round_val:
            l1_cursor = l1_cursor.next or ListNode(0)
            l2_cursor = l2_cursor.next or ListNode(0)
            
            round_val, val = divmod(l1_cursor.val + l2_cursor.val + round_val, 10)
            root_cursor.next = ListNode(val, None)
            root_cursor = root_cursor.next
            
        return root
            
