class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq_list = [0] * 26
        l = 0
        res=0
        for r in range(len(s)):
            ind = ord(s[r]) - ord('A')
            freq_list[ind] += 1

            max_freq = max(freq_list)
            while ((r-l+1) - max_freq > k):
                temp_ind = ord(s[l]) - ord('A')
                freq_list[temp_ind]-=1
                l+=1
            res = max(res, r-l+1)
            
        return res
        