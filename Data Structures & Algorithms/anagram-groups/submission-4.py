class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list)

        for word in strs:
            count = [0] * 26

            for char in word:
                # check how many times each char appears
                position = ord(char) - ord('a')
                count[position] += 1

            key = tuple(count)
            result[key].append(word)

        return list(result.values())

            