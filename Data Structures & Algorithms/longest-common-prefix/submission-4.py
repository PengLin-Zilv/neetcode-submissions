class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # for each string in strs
        # compare each of its char, to the first one (strs[0])
        
        for i in range(len(strs[0])):

            for s in strs[1:]:
                # fail condition: if strs[i] is finished, or if char doesnt match
                if i >= len(s) or s[i] != strs[0][i]:
                    return strs[0][:i]

        return strs[0]
            

