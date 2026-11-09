class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = set()
        if len(nums) < 3:
            return []
        #going with bad solution just to solve
        nums.sort()
        i = 0
        length = len(nums)
        
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                for k in range(j+1, len(nums)):
                    if nums[i] + nums[j] + nums[k] == 0:
                        tmp = [nums[i], nums[j], nums[k]]
                        res.add(tuple(tmp))
        return [list(i) for i in res]


        # d = defaultdict(int)
        # for i in nums:
        #     d[i]+=1
        # for key,value in d.items():
        #     count = value
        #     while count>0:
        #         count-=1

        