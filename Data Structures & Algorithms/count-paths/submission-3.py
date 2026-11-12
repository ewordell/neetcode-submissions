class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0 for _ in range(n)] for _ in range(m)]
        if m==1 and n==1: return 1
        for row in range(m):
            if row == 0:
                for i in range(1,n):
                    dp[0][i] = 1
                continue
            for col in range(n):
                if col == 0:
                    dp[row][col] = 1
                    continue
                dp[row][col] = dp[row-1][col] + dp[row][col-1]
        return dp[m-1][n-1]
        