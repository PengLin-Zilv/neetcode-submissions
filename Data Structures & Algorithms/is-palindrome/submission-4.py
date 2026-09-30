class Solution:
    def isPalindrome(self, s: str) -> bool:
        # giving string s, s reads the same forward and backward

        # example: s = "Was it a car or a cat I saw?"
        # isalnum() checks T/F for letters and numbers
        # we use isalnum() function to skip the space
        l = 0
        r = len(s) - 1

        while l < r:
            if s[l].isalnum() and s[r].isalnum() and s[l].lower() == s[r].lower():
                return False
            l += 1
            r -= 1
        return True
            