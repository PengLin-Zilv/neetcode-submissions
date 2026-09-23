class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        for s in strs:
            key = [0] * 26
            # 26 letters chart
            for c in s:
                key[ord(c) - ord('a')] += 1
            key = tuple(key)
            if key not in d:
                d[key] = []
            d[key].append(s)

        return list(d.values())