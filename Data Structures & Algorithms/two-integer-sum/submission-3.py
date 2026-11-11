class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i,j = -1,-1
        d = defaultdict(list)
        for i, num in enumerate(nums):
            if len(d[num]) > 0:
                return [d[num][0], i]
            d[target - num].append(i)
