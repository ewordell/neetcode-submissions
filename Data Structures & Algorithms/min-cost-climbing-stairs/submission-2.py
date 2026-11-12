class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # dp[i] = min(dp[i-1], dp[i-2])
        # dp[1], dp[2] = 0, 0
# 1, 2, 3, 4

        n = len(cost)
        dp = defaultdict(int) # 0,0
        for i in range(2, n+1):
            dp[i] = min(dp[i-2] + cost[i-2], dp[i-1] + cost[i-1])

        return dp[n] if n > 2 else min(cost[0], cost[1])