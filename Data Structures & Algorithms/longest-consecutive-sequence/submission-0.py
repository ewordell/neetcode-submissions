class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        d = defaultdict(None)
        if len(nums) == 0:
            return 0

        for n in nums:
            d[n] = n+1
        
        final_count=1
        for k,v in d.items():
            count = 1
            temp = k
            while d[temp] in d:
                count +=1
                temp = d[temp]
                final_count = max(final_count, count)

            #this is dogshit
        return final_count