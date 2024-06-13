class Solution:
    def minOperations(self, nums: List[int]) -> int:
        # nums = [1,5,2,4,1]
        # 1, 5, 6, 7, 8
        # 0, 0, 4, 3, 7

        # check if nums arr has more than 1 elem
        # if yes, 
            # iterate through the arr
            # if elem is less than the nxt elem 
                # continue
            # else 
                # get the max elem
        # else, return
        count = 0
        if len(nums) > 1:
            for i in range(len(nums)-1):
                if nums[i] >= nums[i+1]:
                    count += abs(nums[i] - nums[i+1]) + 1
                    nums[i+1] += abs(nums[i] - nums[i+1]) + 1
        return count
