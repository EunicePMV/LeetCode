class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        # for num in nums
        # for digit in num
        # str += str(digit)
        # for ch in str, append to final answer

        final_answer  = []
        for num in nums:
            for digit in str(num):
                final_answer.append(int(digit))
        return final_answer