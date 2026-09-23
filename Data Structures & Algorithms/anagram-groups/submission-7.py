class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        

    # given strs, list of strings
    # return list of lists of anagrams, which that they have the same characters'

    # ["act", "cat", "bab"]
    # returun [["act","cat"], ["bab"]]

    # so first is to find the key and value
    # we will have an empty dictionary
    # the key will be the sorted string, and value will be list of its anagram

        d = {}    # empty dictionary storing {sorted_str: [anagram, ...]}

        for s in strs:
            sorted_s = "".join(sorted(s))  # "act", make this as the key if not exits
            # if "act" already here, append the s
            if sorted_s not in d:
                d[sorted_s] = [s]
            else:
                d[sorted_s].append(s)

        result = []
        for values in d.values():
            result.append(values)
        return result
