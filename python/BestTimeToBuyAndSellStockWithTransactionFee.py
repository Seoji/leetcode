#Runtime: 437ms
#Memory: 23.54MB

class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        pre = [0, -float("inf")]
        for p in prices:
            # 팔때
            p0 = pre[1] + p - fee
            # 살때
            p1 = pre[0] - p

            # 아래 수식을통해 가장 비싸게 팔수있는 타이밍을 찾는다
            if p0 > pre[0]: 
                pre[0] = p0

            # 아래 수식을 통해 가장싸게 살수있는것을 유지한다
            if p1 > pre[1]: 
                pre[1] = p1
        return pre[0]
