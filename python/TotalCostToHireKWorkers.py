#Runtime: 641ms
#Memory: 27.14MB

class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        l, r = 0, len(costs) - 1
        hq1, hq2 = [], []
        heapq.heapify(hq1)
        heapq.heapify(hq2)

        result = 0
        
        while k > 0:
            while(len(hq1) < candidates and l <= r):
                heapq.heappush(hq1, costs[l])
                l += 1
            while(len(hq2) < candidates and l <= r):
                heapq.heappush(hq2, costs[r])
                r -= 1

            
            c1 = hq1[0] if hq1 else float('inf')
            c2 = hq2[0] if hq2 else float('inf')

            if c1 <= c2:
                result += c1
                heapq.heappop(hq1)
            else:
                result += c2
                heapq.heappop(hq2)
            k -= 1

        return result
