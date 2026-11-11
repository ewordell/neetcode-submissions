class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = defaultdict(int)
        res = []
        for n in nums:
            d[n+1000]+=1
        vals = list(d.items())
        vals.sort(key=lambda k: k[1])
        for i in range(-1, -1-k, -1):
            res.append(vals[i][0]-1000)
        return res

