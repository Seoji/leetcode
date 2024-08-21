# Runtime: 579ms
# Memory: 50.65MB

class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        list_len = 0
        middle_idx = 0
        cursor = head
        node_list = []
        

        while cursor:
            node_list.append(cursor)
            cursor = cursor.next
        
        
        if len(node_list)-1 == 1:
            node_list[int(len(node_list)/2) - 1].next = None
        elif len(node_list)-1 == 0:
            head = None
        else:
            node_list[int(len(node_list)/2) - 1].next = node_list[int(len(node_list)/2) +1]

        return head

        
        
