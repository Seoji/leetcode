# Runtime: 269ms
# MemoryUsage: 25.7MB

import math

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [None] * len(nums)
        m = 1
        
        for idx in range(len(nums)):
            num = nums[idx]
            result[idx] = m
            m *= num
        
        m = 1
        for idx in range(len(nums)-1, -1, -1):
            num = nums[idx]
            result[idx] *= m
            m *= num
            
        return result
