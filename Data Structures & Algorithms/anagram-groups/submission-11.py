class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # return [[anagrams, anagrams], [...], [...]]
        
        d = {}

        # we want the key to be the sorted version of the string
        # and the anagrams will be appended or assigned as the value

        for s in strs:
            # we want to have the sorted s
            sorted_s = "".join(sorted(s))
            if sorted_s not in d:
                d[sorted_s] = [s]
            else:
                d[sorted_s].append(s)
        
        result = []
        for values in d.values():
            result.append(values)
        return result