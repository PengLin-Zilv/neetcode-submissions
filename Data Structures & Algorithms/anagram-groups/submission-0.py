class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # O(m * n) m = total number of string  n is avg length of string  
        result = {}

        for word in strs:
            sorted_word = "".join(sorted(word))
            if sorted_word in result:
                result[sorted_word].append(word)
            else:
                result[sorted_word] = [word]

        return list(result.values())