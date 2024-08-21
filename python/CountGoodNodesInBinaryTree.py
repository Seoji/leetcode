# Runtime: 113ms
# Memory: 31.10MB

class Solution:
    result = 0
    def __move(self, cursor, max_val):
        if cursor.val >= max_val:
            self.result += 1
            max_val = cursor.val
        self.__move(cursor.left, max_val) if cursor.left else None
        self.__move(cursor.right, max_val) if cursor.right else None
    def goodNodes(self, root: TreeNode) -> int:
        self.__move(root, root.val)

        return self.result
