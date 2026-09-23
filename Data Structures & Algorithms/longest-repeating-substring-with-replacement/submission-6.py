class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # Question gives string s, example XYYX
        # int k, example 2
        # we want to replace k # of char, get longest character continuity

        # we use sliding windows
        l = 0

        # window failing condition = r - l + 1 - max_count
        # because if the windows has more than k numbers of max_count, it fails

        res = 0
        max_count = 0
        count_dict = {}
        for r in range(len(s)):
            count_dict[s[r]] = count_dict.get(s[r], 0) + 1
            max_count = max(max_count, count_dict[s[r]])
            while r - l + 1 - max_count > k:
                count_dict[s[l]] -= 1
                l += 1
            res = max(res, r-l+1)
        return res

