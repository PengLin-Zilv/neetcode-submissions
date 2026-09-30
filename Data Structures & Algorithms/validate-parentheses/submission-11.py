class Solution:
    def isValid(self, s: str) -> bool:
        # validate if s has valid parentheses

        # when we meet a left parent, we want to pop right parent and return if it
        # == []

        result = []
        
        # example: "[({})]"
        # invalid: "({)"
        # invalid: ")("

        d = {"[": "]", "(": ")", "{": "}"}

        for char in s:
            if char in d.keys():
                result.append(char)
            
            else:
                match = result.pop()
                if d[match] != char:
                    return False
        return result == []

