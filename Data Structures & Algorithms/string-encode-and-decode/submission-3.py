class Solution:

    def encode(self, strs: List[str]) -> str:
        # ["Hello", "World"]
        res = ""
        for string in strs:
            res += str(len(string)) + "e" + string
        return res
        # "5eHello5eWorld"


    def decode(self, s: str) -> List[str]:
        res = []
        i = 0

        while i < len(s):
            j = i
            while s[j] != "e":
                j += 1
            length = int(s[i:j])
            res.append(s[j + 1: j + 1 + length])
        return res
        



