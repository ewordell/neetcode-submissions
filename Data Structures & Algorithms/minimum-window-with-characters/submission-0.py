class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return t
        have = 0
        t_set = set(t)
        need = len(t_set)
        window_dict = defaultdict(int)
        t_dict = defaultdict(int)
        for c in t:
            t_dict[c]+=1
        min_len = float("infinity")
        min_str = [-1,-1]
        
        l = 0
        r = 0
        while r < len(s):
            window_dict[s[r]]+=1
            if window_dict[s[r]] == t_dict.get(s[r], 0):
                have+=1

            while have == need:
                if r-l+1 < min_len:
                    min_len = r-l+1
                    min_str = [l,r]
                window_dict[s[l]] -= 1
                if window_dict[s[l]] < t_dict.get(s[l], 0):
                    have-=1
                l += 1
                
                # window_dict[s]+=1
            r+=1
        
        l,r = min_str
        print(type(l))
        print(type(r))
        return s[l:r+1] if min_len != float("infinity") else ""
