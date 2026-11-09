class Solution:
    # def findMin(self, nums: List[int]) -> int:
    #     r = len(nums)-1
    #     l = 0
    #     res = nums[0]
    #     while l <= r:
    #         if nums[l] < nums[r]:
    #             res = min(res, nums[l])
    #             break
    #         m = (1+r)//2
    #         res = min(res, nums[m])
    #         if nums[m] >= nums[l]:
    #             l=m+1
    #         else:
    #             r=m-1
    #     return res

    def findMin(self, nums: List[int]) -> int:
        res = nums[0]
        l, r = 0, len(nums) - 1

        while l <= r:
            if nums[l] < nums[r]:
                res = min(res, nums[l])
                break

            m = (l + r) // 2
            res = min(res, nums[m])
            if nums[m] >= nums[l]:
                l = m + 1
            else:
                r = m - 1
        return res
    
        