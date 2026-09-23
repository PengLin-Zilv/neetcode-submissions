class Solution:
    def isValid(self, s: str) -> bool:
        # empty stack
        # pop, we will pop the latest
        # we will pop the s, add to stack
        # and then pop the stack to see if stack = []
        stack = []

        d = {'[': "]", '(': ")", "{": "}"}

        # s = "[({})]"
        # stack = "[({"

        for char in s:
            if char in d.keys():
                stack.append(char)

            elif char in d.values():
                if stack == []:
                    return False
                top = stack.pop()
                if d[top] != char:
                    return False
        return stack == []
                