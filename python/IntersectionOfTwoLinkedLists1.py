# Runtime: 78 ms
# Memory Usage: 27.2 MB

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        cursorA, cursorB = headA, headB, 
        idx1, idx2 = 0, 0
        while headA: 
            headA, idx1 = headA.next, idx1 + 1
        while headB: 
            headB, idx2 = headB.next, idx2 + 1    

        while idx1 > idx2: 
            cursorA, idx1 = cursorA.next, idx1 - 1
        while idx2 > idx1: 
            cursorB, idx2 = cursorB.next, idx2 - 1
        
        while cursorA != cursorB: 
            cursorA, cursorB = cursorA.next, cursorB.next
        return cursorA
