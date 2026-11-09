class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0 
        r = l+1
        l_sub:int=1 if len(s) > 0 else 0
        if l_sub == 0:
            return 0
        cur_str = s[l]
        while r < len(s):
            cur_str = s[l:r+1]
            if len(cur_str) == len(set(cur_str)):
                r+=1
                l_sub = max(len(cur_str), l_sub)
            else:
                l+=1
                r+=1
        return l_sub