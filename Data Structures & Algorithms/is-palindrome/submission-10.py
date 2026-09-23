class Solution:
    def isPalindrome(self, s: str) -> bool:
        # we have a string s
        # want to know if it is palindrome
        # want to check l and r, if l and r is not alphanumeric chars, skip
        # s[l] != s[r], return False

        l = 0
        r = len(s) - 1
        
        while l < r:
            while l < r and not s[l].isalnum():
                l += 1
            while l < r and not s[r].isalnum():
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l +=1
            r -= 1
        return True