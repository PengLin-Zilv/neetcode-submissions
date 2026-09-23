class Solution:
    def isPalindrome(self, s: str) -> bool:
        # given a string s
        newStr = ''

        for c in s: 
            if c.isalnum():
                newStr += c.lower()
        return newStr == newStr[::-1]