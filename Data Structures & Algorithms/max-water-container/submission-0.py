class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1
        max_area = 0
        while l < r:
            # print(f"l {l}")
            # print(r)
            print(max_area)
            dif = r - l
            height = min(heights[l], heights[r])
            prod = height * dif
            max_area = max(prod, max_area)
            print(max_area)

            if heights[l] < heights[r]:
                l+=1
            else:
                r-=1
            
        return max_area

        
        