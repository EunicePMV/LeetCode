class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        elem_sum = sum(nums)
        # loop through the arr of nums
        # convert it into string
        # using loop, loop through char of digit str
        # convert ch to int, then add
        digit_sum = 0
        for n in nums:
            for ch in str(n):
                digit_sum += int(ch)

        return abs(elem_sum - digit_sum)
        