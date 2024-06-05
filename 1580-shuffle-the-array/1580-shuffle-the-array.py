class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        ans = []

        first_nums = nums[:n]
        second_nums = nums[n:]
        for i in range(len(first_nums)):
            ans.append(first_nums[i])
            ans.append(second_nums[i])

        return ans