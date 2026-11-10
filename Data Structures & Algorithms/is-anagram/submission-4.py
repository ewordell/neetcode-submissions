class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s_dict = {}
        t_dict = {}
        for i in range(26):
            s_dict[i] = 0
            t_dict[i] = 0
        for (s_char, t_char) in zip(s,t):
            s_dict[ord(s_char) - 97]+=1
            t_dict[ord(t_char) - 97]+=1
        return s_dict == t_dict
        