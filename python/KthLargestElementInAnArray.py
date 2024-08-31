#Runtime: 518ms 
#Memory: 29.62MB

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums = list(map(lambda num: num * -1, nums))
        heapify(nums)
        result = None
        for _ in range(0, k):
            result = heapq.heappop(nums)
        
        return result * -1
