class Solution:
    def isPalindrome(self, s: str) -> bool:
        # giving string s, s reads the same forward and backward

        # example: s = "Was it a car or a cat I saw?"
        # isalnum() checks T/F for letters and numbers
        # we use isalnum() function to skip the space
        l = 0
        r = len(s) - 1

        while l < r:
            while l < r and s[l].isalnum() == False:
                l += 1
            while l < r and s[r].isalnum() == False:
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1
        return True
            