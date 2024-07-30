# Runtime: 584ms
# MemoryUsage: 17MB


class Solution:

    def coinChange(self, coins: List[int], amount: int) -> int:

        dp = [0] + [float('inf')] * amount
        for i in range(1, amount + 1): 
            # i-coin 이였을때보다 코인 하나를 더쓰는거니까 +1 처리
            dp[i] = min([dp[i - coin] if i - coin >= 0 else float('inf') for coin in coins]) + 1
        return dp[amount] if dp[amount] != float('inf') else -1
