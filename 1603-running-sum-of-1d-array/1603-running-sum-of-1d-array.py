class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        sum_of_nums = []
        total = 0
        for i in range(len(nums)):
            total += nums[i]
            sum_of_nums.append(total)
        return sum_of_nums

        