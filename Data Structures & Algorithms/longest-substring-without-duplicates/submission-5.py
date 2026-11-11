class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #abcabd --> 4
        if len(s) == 0:
            return 0
        res = 1
        l,r = 0,0
        char_set = set(s[l])
        while r < len(s):
            r+=1
            if r == len(s):
                return res
            elif s[r] in char_set:
                while s[l] != s[r]:
                    char_set.remove(s[l])
                    l+=1
                l+=1
            else:
                char_set.add(s[r])
                res = max(res, r-l+1)
        return res
            