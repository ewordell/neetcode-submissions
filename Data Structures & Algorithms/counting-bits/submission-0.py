class Solution:
    def countBits(self, n: int) -> List[int]:
        res = [0] * (n+1)
        for i in range (1,n+1):
            count = 0
            for j in bin(i):
                count = count + 1 if j=="1" else count
            res[i] = count
        return res
        