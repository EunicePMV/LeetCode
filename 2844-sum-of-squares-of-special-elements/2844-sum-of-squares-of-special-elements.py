class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        # init n length, 
        n = len(nums)
        ans = 0

        # loop through first the array
        for i in range(len(nums)):
            if n % (i+1) == 0:
                ans += nums[i]**2
        return ans 