class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # 简化版

        d= {}
        
        for s in strs:
            sorted_s = "".join(sorted(s))

            if sorted_s not in d:
                d[sorted_s] = [s]
            else:
                d[sorted_s].append(s)
        return list(d.values())


        # Time Complexity: O(n * m log m)
        # n is the length of the list
        # m is the length of the single str
        # and for sorting m, m log m
        # so O(n m log m)
