# Runtime: 1847ms
# MemoryUsage: 16.8MB

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        result = [1] * len(nums)
        for right in range(1, len(nums)):
            num_right = nums[right]
            for left in range(0, right):
                num_left = nums[left]
                if num_right > num_left:
                    result[right] = max(
                        result[right], 
                        result[left]+1
                    )
        return max(result)
