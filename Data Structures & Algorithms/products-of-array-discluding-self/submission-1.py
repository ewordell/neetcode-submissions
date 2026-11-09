class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l = len(nums)
        outputs = [0] * l
        for i,n in enumerate(nums):
            s_1 = nums[0:i]
            s_2 = nums[i+1:]
            prod = 1
            for j in s_1:
                prod *= j
            for j in s_2:
                prod *= j
            outputs[i] = prod
        return outputs
