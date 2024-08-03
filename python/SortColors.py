# Runtime: 28ms
# MemoryUsage: 16.4MB

class Solution:
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        red_idx, white_idx, blue_idx = 0, 0, len(nums)-1
        
        while white_idx <= blue_idx:
            if nums[white_idx] == 0:
                nums[white_idx], nums[red_idx] = nums[red_idx], nums[white_idx]
                white_idx += 1
                red_idx += 1
            elif nums[white_idx] == 1:
                white_idx += 1
            elif nums[white_idx] == 2:
                nums[white_idx], nums[blue_idx] = nums[blue_idx], nums[white_idx]
                blue_idx -= 1
            else:
                pass
        
        
