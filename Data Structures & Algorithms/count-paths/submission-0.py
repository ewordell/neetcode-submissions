class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        top_row = [0] * n
        for row in range(m):
            for i, row in enumerate(top_row):
                if m==0:
                    top_row[i] = 1
                    continue
                elif i==0:
                    top_row[i] = 1
                else:
                    top_row[i] = top_row[i] + top_row[i-1] 
        return top_row[-1]
        