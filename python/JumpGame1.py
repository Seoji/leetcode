# Runtime: 799ms
# MemoryUsage: 17.8MB


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        cursor = 0
        nums = list(map(lambda x: sum(x), enumerate(nums) ))
        
        while cursor < len(nums)-1:
            if nums[cursor] == cursor:
                return False
            sliced_nums = nums[cursor+1:nums[cursor]+1]
            max_num = max(sliced_nums)
            max_num_idx = sliced_nums.index(max_num) + cursor +1
            
            if max_num_idx >= len(nums) -1:
                return True
            elif cursor == max_num_idx:
                return False
            else:
                cursor = max_num_idx
        else:
            return True
            
