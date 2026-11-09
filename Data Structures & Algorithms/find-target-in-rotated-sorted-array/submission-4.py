class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        res = -1
        
        while l < r:
            m = (l+r)//2
            if nums[m] > nums[r]:
                l = m + 1
            else:
                r = m
        pivot = l
        print(pivot) #idk how this works tbh i dont understand

        if nums[pivot] <= target and target <= nums[len(nums) - 1]:
            l = pivot
            r = len(nums) - 1
        else:
            l = 0
            r = pivot

        while l <= r:
            m = (l+r)//2
            if nums[m] == target:
                res = m
                break
            elif nums[m] < target:
                l = m + 1
            else:
                r = m-1
        return res

        
        