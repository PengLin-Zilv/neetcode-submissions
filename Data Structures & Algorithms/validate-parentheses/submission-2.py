class Solution:
    def isValid(self, s: str) -> bool:
        # check if the string contains valid parenthesis

        stack_dict = {'[': "]", '(': ")", "{": "}"}
        stack = []
        for char in s:
        # example string: ({[]})

# for [, stack = ['[']

# stack = ['({['] after 3 loops

# for 4th one, char = "]"

# stack now = ['({']

# now: 
# 1. stack cannot be empty (because then means uneven brackets)
# 2. pop the top from the stack 
# 3. the top one have to be = char


            # if open bracket, append char
            if char in stack_dict.keys():
                stack.append(char)

            # if closed brackey, pop char and check if match
            elif char in stack_dict.values():
                if not stack:
                    return False
                top = stack.pop()
                if stack_dict[top] != char:
                    return False


        return stack == []

