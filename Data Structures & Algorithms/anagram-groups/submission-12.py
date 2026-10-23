class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # strs is a list of strings
        # goal: group all anagrams together into sublists
        # return list of lists of anagrams (anagram = words with same chars)

        # strs = ["act", "pots", "tops", "cat", "stop", "hat"]


        # so we want to for each word, sort them, see if match in the dict, if yes add to value
        # return list of values

        # first create a dictionary, store [anagram: [anagram_list], ...]

        # for each str in strs:
        # if they are in the dict, append them to the value list
        # if they are not in dict, d[sorted_str] = [str]

        # result = []
        # for anagram, anagram_list in d.items():
        #   result.append(anagram_list)

        d = {}
        # initialize an empty dict storing {sorted_word: [word_list], ...}

        for word in strs:
            # for each word, we find its sorted version, and see if match to words in d already
            sorted_word = "".join(sorted(word))
            if sorted_word in d:
                # if the sorted version match, then we simply append the word to the word_list
                d[sorted_word].append(word)
            else:
                # if not in d, then we initialize key: value (sorted_word: [word_list])
                d[sorted_word] = [word]
        
        result = []
        # initialize a result list

        for sorted_word, word_list in d.items():
            # find the value list, each word_list is a list of anagrams
            # add each anagram list to the result list
            result.append(word_list)
        return result







