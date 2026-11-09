class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        if len(nums) == 0:
            return False
        nums_dict = {}
        for item in nums: 
            if nums_dict.get(item, None):
                return True
            nums_dict[item] = 1
        return False