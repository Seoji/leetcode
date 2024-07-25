# Runtime: 32ms
# MemoryUsage: 17.5MB

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        cursor = head
        copied_node_list = []
        node_idx_dict = dict()
        
        node_idx = 0
        while cursor:
            copied_node_list.append(Node(x=cursor.val, random=cursor.random))
            node_idx_dict[cursor] = node_idx
            cursor = cursor.next
            node_idx += 1
            
            
        for copied_node_idx, copied_node in enumerate(copied_node_list):
            if copied_node.random in node_idx_dict:
                copied_node.random = copied_node_list[node_idx_dict[copied_node.random]]
            
            if copied_node_idx > 0:
                copied_node_list[copied_node_idx-1].next = copied_node
                
        return copied_node_list[0]
                
            
