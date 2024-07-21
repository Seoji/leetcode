# Runtime: 6794ms
# MemoryUsage: 33.1MB

class Solution:
    def maxCoins(self, nums):
        cache_dict = dict()
        # filtering useless zero
        # pad 0
        nums = [1] + list(filter(lambda num: num, nums)) + [1]
        def __burst(left, right):
            # not enough range
            if right - left == 1:
                return 0
            if (left, right) not in cache_dict:
                # i is last man standing
                cache_dict[(left, right)] = max(nums[left] * nums[i] * nums[right] + __burst(left, i) + __burst(i, right) for i in range(left + 1, right))
            return cache_dict[(left, right)]
        return __burst(0, len(nums) - 1)


