class Solution:
    def isValid(self, s: str) -> bool:
        d = {"[": "]", "(": ")", "{": "}"}
        stack = []

        for parenthesis in s:
            if parenthesis in d.keys():
                stack.append(parenthesis)
                
            elif parenthesis in d.values():
                if not stack:
                    return False
                top = stack.pop()
                if d[top] != parenthesis:
                    return False
        return stack == []
                