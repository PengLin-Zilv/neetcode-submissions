class Solution:

    def encode(self, strs: List[str]) -> str:
        # ["Hello", "World"]
        res = ""
        for string in strs:
            res += str(len(string)) + "e" + string
        return res

    def decode(self, s: str) -> List[str]:
        # "5eHello5eWorld"
        i = 0
        res = []

        while i < len(s):
            j = i # j = 0
            while s[j] != "e":
                j += 1
            length = int(s[i:j])
            word = s[j+1: j + 1 + length]
            res.append(word)
            i = j + 1 + length
        return res
            





