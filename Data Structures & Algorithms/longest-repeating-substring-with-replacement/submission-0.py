class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # given s: all uppercase English letter
        # given k, int
        # we want to replace k chars to have the max single char continuity

        # idea: we will have l and r, r will slide
        # l will slide only if invalid
        # invalid here will be that: if the window breaks the k int


        count = {}

        l = 0
        max_count = 0
        res = 0


        for r in range(len(s)):
            # window breaks
            window_length = r - l + 1
            if s[r] in count:
                count[r] += 1
            count[r] = 1
            max_count = max(count.values())

            while window_length - max_count > k:
                count[s[l]] -= 1
                l += 1
            res = max(res, count[s[r]])
        return res

