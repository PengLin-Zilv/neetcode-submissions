class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned = ""             # first step is to create an empty string
        for char in s:           # if s is alphanumeric character, then add to cleaned string
            if char.isalnum():
                cleaned += char.lower()
        
        left = 0                   # set the left pointer = 0
        right = len(cleaned) - 1    # set the right pointer = len of cleaned -1
        while left < right:         # while they didn't meet each other
            if cleaned[left] != cleaned[right]:
                return False                 # if they don't macth, return false
            left += 1
            right -= 1                # compare next one
        return True                   # return True if left = right!
        