# Runtime: 574 ms
# Memory Usage: 20.7 MB

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        
        for idx, num in enumerate(nums):
            if idx > 0 and nums[idx-1] == num:
                continue
            if num > 0:
                continue
                
            left_cursor = idx + 1
            right_cursor = len(nums) - 1
            while left_cursor < right_cursor:
                
                sum_nums = num + nums[left_cursor] + nums[right_cursor]
                
                if sum_nums == 0:
                    result.append([num, nums[left_cursor], nums[right_cursor]])
                    while(nums[left_cursor] == nums[left_cursor+1] and left_cursor+1 < right_cursor):
                        left_cursor += 1
                    left_cursor += 1
                    while((nums[right_cursor] == nums[right_cursor-1])  and left_cursor < right_cursor-1):
                        right_cursor -= 1
                    right_cursor -= 1
                
                if sum_nums < 0:
                    left_cursor += 1
                    
                if sum_nums > 0:
                    right_cursor -= 1
                    
        return result
