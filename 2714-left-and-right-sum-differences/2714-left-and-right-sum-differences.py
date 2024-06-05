class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        left = 0
        right = sum(nums)
        answer = []
        for n in nums:
            right -= n
            answer.append(abs(left - right))
            left += n
        return answer