# Runtime: 177ms
# Memory: 30.06MB

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# mine
# class Solution:
#     result = 0
#     def longestZigZag(self, root: Optional[TreeNode]) -> int:
#         def __travel(cursor, cnt, next_direction):
#             if next_direction == "left":
#                 if cursor.left:
#                     self.result = max(cnt+1, self.result)
#                     __travel(cursor.left, cnt+1, "right")
#                 if cursor.right:
#                     __travel(cursor.right, 1, "left")
#             if next_direction == "right":
#                 if cursor.right:
#                     self.result = max(cnt+1, self.result)
#                     __travel(cursor.right, cnt+1, "left")
#                 if cursor.left:
#                     __travel(cursor.left, 1, "right")
            


#         __travel(root, 0, "left")
#         __travel(root, 0, "right")

#         return self.result

class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        self.maxi = 0

        def dfs(node, left, right):
            self.maxi = max(self.maxi, left, right)

            if node.left:
                dfs(node.left, right + 1, 0)

            if node.right:
                dfs(node.right, 0, left + 1)

        dfs(root, 0, 0)
        return self.maxi

