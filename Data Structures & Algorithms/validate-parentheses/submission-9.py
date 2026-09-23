class Solution:
    def isValid(self, s: str) -> bool:
        res = []
        d = {"{": "}", "[": "]", "(": ")"}

        for char in s:
            if char in d.keys():
                res.append(char)
            elif char in d.values():
                if not res:
                    return False
                top = res.pop()
                if d[top] != char:
                    return False
        return res == []

        # "[][]("