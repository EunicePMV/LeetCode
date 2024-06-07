class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        ans = []
        for i in range(len(nums) // 2):
            freq = nums[2*i]
            value = nums[2*i+1]
            for n in range(freq):
                ans.append(value)
        return ans
        