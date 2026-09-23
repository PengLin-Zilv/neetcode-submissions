class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list)

        for word in strs:
            count = [0] * 26

            for char in word:
                # check how many times each char appears
                position = ord(char) - ord('a')
                count[position] += 1
                # update the count of the position

            key = tuple(count)
            result[key].append(word)

        return list(result.values())

            
# time complexity: outer loop m * inner loop n times O(1)
# = O(m x n)
# m = amount of words, n = avg length of the word

# space complexity = O(m x n)