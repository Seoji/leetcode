# Runtime: 37ms
# Memory: 16.54MB

# just fucking pattern
class Solution:
    def numTilings(self, n: int) -> int:
        MOD = 10**9 + 7
        
        if n == 1:
            return 1
        elif n == 2:
            return 2
        elif n == 3:
            return 5
        
        f = [0] * (n + 1)
        g = [0] * (n + 1)
        f[1], f[2], f[3] = 1, 2, 5
        g[2], g[3] = 1, 2
        
        for i in range(4, n + 1):
            g[i] = (f[i-2] + g[i-1])
            f[i] = (f[i-1] + f[i-2] + 2 * g[i-1])
            f[i] = f[i-1]*2 + f[i-3]
        
        return f[n]% MOD      
