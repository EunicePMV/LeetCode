class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        # init n length, 
        n = len(nums)
        ans = 0

        # loop through first the array
        for i in range(1, len(nums)+1):
            if n % i == 0:
                ans += nums[i-1]**2
        return ans 