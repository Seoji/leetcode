# Runtime: 37ms
# MemoryUsage: 16.7MB

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = [[]]
        for num in nums:
            result += [elem + [num] for elem in result]
        return result
        
