class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        # dict with the key value pair of elements and their frequency
        # check the max value through their values 
        # if there is duplicate then add to the final ans

        elem_freq = {}
        for num in nums:
            if num in elem_freq:
                elem_freq[num] += 1
            else:
                elem_freq[num] = 1
        
        max_freq = max(elem_freq.values())
        final_ans = 0
        for freq in elem_freq.values():
            if freq == max_freq:
                final_ans += freq
        return final_ans
        