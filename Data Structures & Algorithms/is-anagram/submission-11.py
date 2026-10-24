from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # given 2 strings s and t
        # return true if they contain same chars
        # they are all lowercase letters

    # we use Counter
    # which counts the appearance of the letter in s and t
    # return if they are same
        s_dict = Counter(s)
        t_dict = Counter(t)

        return s_dict == t_dict

