#Runtime: 37ms
#Memory: 16.60MB

class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        stack = [(0, [], 0, k)]
        nums = range(1, 10)
        result = []

        while stack:
            sm, tmp, index, k_val = stack.pop(0)

            for i in range(index, len(nums)):
                if sm + nums[i] < n and k_val != 1:
                    stack.append([
                        sm+nums[i],
                        tmp + [nums[i]],
                        i+1,
                        k_val-1
                    ])
                elif sm+nums[i] == n and k_val == 1:
                    result.append(
                        tmp + [nums[i]]
                    )
        return result
