class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        # solution 1:
        # 1. access list of nums 
        # 2. append the nums in the new arr
        ans = []
        for i in range(len(nums)):
            ans.append(nums[nums[i]])
        
        return ans