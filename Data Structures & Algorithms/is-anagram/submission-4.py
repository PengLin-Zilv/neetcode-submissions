class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # 1. restate problem/ clarify edge cases
        # 2. state my approach with time/space complexity
        # 3. talk while writing codes
        # 4. test with a simple example manually

        # isAnagram:
        # given s and t, return true if they are anagrams of each other
        # else, if not return false

        # my thinking process will be,
        # we need the same length, same characters

        # so i will be using a dictionary, like a seen dict, to store # of seen characters in s
        # so space complexity will be O(n) because it based on the length of the strings
        # the time complexity will be O(n + m) which is O(2n) = O(n)

        seen_s = {}
        seen_t = {}
        if len(s) != len(t):
            return False
        
        for char in s:
            if char in seen_s:
                seen_s[char] += 1
            else:
                seen_s[char] = 1

        for char in t:
            if char in seen_t:
                seen_t[char] += 1
            else:
                seen_t[char] = 1

        return seen_s == seen_t

        




        