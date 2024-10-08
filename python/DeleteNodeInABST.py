# Runtime: 48ms
# Memory: 19.90MB

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root, key):
        """
        :type root: TreeNode
        :type key: int
        :rtype: TreeNode
        """
        if not root: return
        if root.val > key: root.left = self.deleteNode(root.left, key)
        elif root.val < key: root.right = self.deleteNode(root.right, key)
        else:
            if not root.right: return root.left
            elif not root.left: return root.right
            tmp, mini = root.right, root.right.val
            while tmp.left:
                tmp, mini = tmp.left, tmp.left.val
            root.val, root.right = mini, self.deleteNode(root.right, mini)
        return root
        
            
            


