class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        o_count = 0
        c_count = 0
        if len(s) % 2:
            return False
        d= {
            "(": ")",
            "[": "]",
            "{": "}"
        }

        for c in s:
            if c in d.keys():
                stack.append(d[c])
                o_count += 1
            else:
                if len(stack) == 0 or c != stack.pop():
                    return False
                c_count += 1
        return o_count == c_count