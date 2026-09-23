class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        d = {"(": ")", "[": "]", "{": "}"}

        for char in s:
            if char in d.keys():
                stack.append(char)

            elif char in d.values():
                if not stack:
                    return False
                top = stack.pop()
                if d[top] != char:
                    return False
        return stack == []