# Runtime: 432ms
# Memory: 21.82MB

class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        nums_count = len(nums)
        count_of_zero = nums.count(0)

        if count_of_zero == 1:
            return nums_count-1
        elif count_of_zero == 0:
            return nums_count-1
        else:
            result = 0
            zero_idx_list = [ idx for idx, num in enumerate(nums) if not num]
            for idx in range(0, len(zero_idx_list)):
                if idx == 0:
                    result = max(result, zero_idx_list[1]-1)
                elif idx == len(zero_idx_list) - 1:
                    result = max(result, (zero_idx_list[idx]  - zero_idx_list[idx-1]-1) + (len(nums)-1 - zero_idx_list[idx])  )
                else:
                    result = max(result, zero_idx_list[idx+1] - zero_idx_list[idx-1] - 2 )
            
            return result
                
