class Solution:
    def isPalindrome(self, s: str) -> bool:
        # s is a string
        # check if it is same reading forward and backward

        # use isalnum(), this is a func tells us if this char is letters/nums or no

        l = 0
        r = len(s) - 1

        while l < r:
            # it ignores the non alphanumeric chars, so we want to skip them
            # the main thing we want to check is, if s[l] != s[r], return False
            while l < r and s[l].isalnum() == False:
                    l += 1
            while l < r and s[r].isalnum() == False:
                    r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1
        return True

