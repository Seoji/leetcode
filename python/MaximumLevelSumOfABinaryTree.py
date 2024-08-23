# Runtime: 164ms
# Memory: 19.68MB

class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        result = 1
        max_sum = root.val
        lv = 1
        q = deque([root])

        while q:
            temp = []
            lv += 1
            while q:
                node = q.popleft()
                if node.left:
                    temp.append(node.left)
                if node.right:
                    temp.append(node.right)
            # 아래 조건식을 넣지않으면 temp 가 [] 인 경우에 대한 처리가 일어나고
            # node 들이 음수일경우 temp 가 [] 이고 cur_sum 이 0인 케이스가 정답이 되어버린다
            if temp:
                for node in temp:
                    q.append(node)
                cur_sum = reduce(lambda acc, cur: acc + cur.val, temp, 0)
                if cur_sum > max_sum:
                    max_sum = cur_sum
                    result = lv
        return result
