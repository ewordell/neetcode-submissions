class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        for s in strs:
            sort_str = "".join(sorted(s))
            
            if sort_str in d:
                d[sort_str].append(s)
            else:
                d[sort_str] = [s]
        return [d[k] for k in d]
        
                