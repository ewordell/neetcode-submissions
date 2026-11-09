class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        l = [0] * 2000
        k_list = [0] * k
        for n in nums:
            l[n+1000]+=1
        for i in range(k):
            val = max(l)
            index = l.index(val)
            k_list[i] = index - 1000
            l[l.index(val)] = 0
        return k_list
