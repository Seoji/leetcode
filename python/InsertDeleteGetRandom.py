# Runtime: 251ms
# MemoryUsage: 63.9MB

class RandomizedSet:
    def __init__(self):
        self.nums = [] 
        self.ind = {}
    def insert(self, val):
        if val not in self.ind: 
            self.nums.append(val)
            self.ind[val] = len(self.nums) - 1
            return True
        return False
    
    
    def remove(self, val):
        if val in self.ind:
            ind, last = self.ind[val], self.nums[-1]
            self.nums[ind], self.ind[last] = last, ind
            self.nums.pop()
            self.ind.pop(val)
            return True
        return False


    def getRandom(self):
        return random.choice(self.nums)

