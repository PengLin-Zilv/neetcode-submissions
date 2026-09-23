class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list)

        for word in strs:  # loop over every word
            # create character counter
            char_count = [0] * 26

            # count how many times each word appears
            for char in word:
                position = ord(char) - ord('a')
                char_count[position] += 1
            key = tuple(char_count)
            result[key].append(word)
        return list(result.values())
            