class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # sorting and hash map
        # for this question, form a dictionary that contains:
        # key as the number, value as the # of counts

        # nums = [1,1,3,2,2]

        count_dict = {}
        for n in nums:
            count_dict[n] = 1 + count_dict.get(n, 0)
        # now count_dict became the dict that has key: value which is the num: its index
        # {1:2, 3:1, 2:2}
        # Next step, turn this into list
        count_list = []
        for key, val in count_dict.items():
            count_list.append([val, key])
        # so the list will be
        # [[2,1], [1,3], [2,2]]

        # Next step, sort this to make it become list of [count,num] but from least to most freq
        count_list.sort()
        # now we have [[1,3], [2,1], [2,2]]

        # Next step, get the first k frequency from the rightmost side, which is the top
        top_k_freq_list = []
        while len(top_k_freq_list) < k:
            top_k_freq_list.append(count_list.pop()[1])
        return top_k_freq_list

        # Time Complexity: O(n log n)
        # Space Complexity: O(n)
