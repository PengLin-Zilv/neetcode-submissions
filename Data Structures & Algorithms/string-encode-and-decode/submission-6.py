class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for string in strs:
            res += str(len(string)) + "#" + string
        return res

        # ["Hello", "World"] -> "5#Hello5#World"
    def decode(self, s: str) -> List[str]:
        res = []
        # we returning a string to a list of strings
        # the string start with its length, eg. 5,10...
        # and then a separator "#"

        i = 0
        while i < len(s):
            j = i  #so j = 0, and j equals to the length if the length is 1 digit, 
            # but we need to check if two digits or more
            while s[j] != "#":
                j += 1
            # now j arrives at "#"
            length = int(s[i:j])
            # 5
            i = j + 1 + length
            word = s[j+1:i]
            res.append(word)
        return res