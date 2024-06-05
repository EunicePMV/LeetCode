class Solution:
    def sumIndicesWithKSetBits(self, nums: List[int], k: int) -> int:
        total = 0
        # loop through the number of elements through indices
        for i in range(len(nums)):
            # convert this num into binary 
            bits_num = bin(i)

            # count the occurrences of set of bits '1'
            if bits_num.count('1') == k:
                total += nums[i]
            count = 0
        return total