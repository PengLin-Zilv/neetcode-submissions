class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return ""

        # encode means to just turn the list to a stringr
        result = ""
        for s in strs:
            letter_count = len(s)
            result += str(letter_count) + "#" + s
        return result

        # strs = ["Hello", "World"]
        # result = "5#Hello5#World"

    def decode(self, s: str) -> List[str]:
        # decode gives back ["Hello", "World"]
        # s = "5#Hello5#World"
        # goal: res = ['Hello', 'World']

        res = []
        i = 0

        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])  # index 0, extract the number
            i = j + 1
            j = i + length
            # j jump to the next number
            res.append(s[i:j])
            i = j

        return res




