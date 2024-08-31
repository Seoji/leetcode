#Runtime: 769ms
#Memory: 37.07MB


class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        result = 0

        nums_list = sorted([(num2, num1) for num1, num2 in zip(nums1, nums2)], reverse=True)
        hq = []
        heapq.heapify(hq)

        for idx in range(0, k-1):
            heapq.heappush(hq, nums_list[idx][1])

        sum_hq = sum(hq)
        for idx in range(k-1, len(nums1)):
            num1 = nums_list[idx][1]

            sum_hq += num1

            heapq.heappush(hq, num1)

            result = max(result, sum_hq * nums_list[idx][0])

            sum_hq -= heapq.heappop(hq)

        return result
