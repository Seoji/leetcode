# Runtime: 83 ms
# Memory Usage: 21 MB

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequent_dict = dict()

        for num in nums:
            if num in frequent_dict:
                frequent_dict[num] += 1
            else:
                frequent_dict[num] = 1
        return sorted(list(frequent_dict.keys()), key=lambda x: frequent_dict[x], reverse=True)[:k]
