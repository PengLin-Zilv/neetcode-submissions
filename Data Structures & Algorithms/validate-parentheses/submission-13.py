class Solution:
    def isValid(self, s: str) -> bool:
        # check if the string contains valid parenthesis

        pair = {'[': "]", '(': ")", "{": "}"}
        result = []

        for char in s:
            if char in pair.keys():
                result.append(char)
            else:
                # char is right parentheses
                # if valid, we pop the last in the result stack
                # ()(), or ([])
                # when we met ) we pop (, or ] we pop [
                # or if we have empty stack which starts with right parent
                if not result: # base case
                    return False
                
                # then check if the right parent match with the result
                top = result.pop()
                if pair[top] != char:
                    return False
        return result == []
