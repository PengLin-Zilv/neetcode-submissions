class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        res = 0
        max_count = 0

        l = 0

        for r in range(len(s)):
            count[s[r]] = count.get(s[r], 0) + 1
            # count s[r]
            max_count = max(max_count, count[s[r]])

            # window failing condition
            while r - l + 1 - max_count > k:
                count[s[l]] -= 1
                l += 1
            res = max(res, r-l+1)
        return res
            