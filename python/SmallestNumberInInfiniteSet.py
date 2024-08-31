#Runtime: 96ms
#Memory: 17.20MB

class SmallestInfiniteSet:
    def __init__(self):
        self.hq = []
        self.counter = 1
        heapq.heapify(self.hq)

    def popSmallest(self) -> int:
        if self.hq:
            val = heapq.heappop(self.hq)
            while self.hq:
                next_val = heapq.heappop(self.hq)
                if val != next_val:
                    heapq.heappush(self.hq, next_val)
                    break
            return val
        else:
            result = self.counter
            self.counter += 1
            return result

        

    def addBack(self, num: int) -> None:
        if num < self.counter:
            heapq.heappush(self.hq, num)
        else:
            pass
        

