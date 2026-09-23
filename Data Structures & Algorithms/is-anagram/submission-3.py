class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # s and t, check if they contain the same characters

        # return sorted(s) == sorted(t)


        # counter

        s_count = Counter(s)
        t_count = Counter(t)

        return s_count == t_count