# Runtime: 28ms
# Memory: 16.55MB

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        q = deque([root])
        result = [root.val]

        while q:
            temp = []
            while q:
                node = q.popleft()
                if node.left:
                    temp.append(node.left)
                if node.right:
                    temp.append(node.right)
            if temp:
                result.append(temp[-1].val)
                for node in temp:
                    q.append(node)
        return result
            
