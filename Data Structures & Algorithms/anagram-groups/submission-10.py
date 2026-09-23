class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # give an array of strings
        # anagram is a strings contains exact same characters as another string

        # return list of list of anagram
        # first we think of anagram, so sorted[str], "bac" will be "abc"

        # so for every string, we will need to sort them, 
        # if they not on dictionary, add to dictionary, sorted version will be the key
        # and the values will be the anagrams

        # time complexity: O(n x k log k) since we storing on a dict
        # space complexity: O(n x k) since

        d = {}

        for s in strs:
            string_key = "".join(sorted(s))
            if string_key not in d:
                d[string_key] = [s]
            else:
                d[string_key].append(s)
        return list(d.values())