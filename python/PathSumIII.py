# Runtime: 181ms
# Memory: 20.71MB

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    result = 0
    target_sum = 0
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        if not root:
            return self.result
        self.target_sum = targetSum

        def __travel(cursor, val_list):
            val_list_sum = sum(val_list)
            for idx in range(0, len(val_list)):
                if val_list_sum == self.target_sum:
                    self.result += 1
                val_list_sum -= val_list[idx]

            __travel(cursor.left, val_list + [cursor.left.val]) if cursor.left else None
            __travel(cursor.right, val_list + [cursor.right.val]) if cursor.right else None
        __travel(root, [root.val])
        return self.result
        
