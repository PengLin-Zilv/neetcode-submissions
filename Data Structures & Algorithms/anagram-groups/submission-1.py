class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # empty dictionary for result
        result = defaultdict(list) # mapping charCount to list of anagrams
        
        for s in strs:
            # a ... z
            count = [0] * 26

            for char in s:
                count[ord(char) - ord("a")] += 1

            result[tuple(count)].append(s)
        return list(result.values())