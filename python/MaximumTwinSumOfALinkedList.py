# Runtime: 354ms
# Memory: 44.49MB

class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        cursor = head
        node_list = []
        sum_list = []
        
        while cursor:
            node_list.append(cursor.val)
            cursor = cursor.next
        
        node_list_len = len(node_list)
        for idx in range(0, int(node_list_len/2)):
            sum_list.append(node_list[idx]+node_list[node_list_len-idx-1])

        return max(sum_list)
            

        
