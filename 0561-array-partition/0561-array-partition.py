class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        # sort the arr
        # nums.sort()
        
        # # store final ans
        # final_ans = 0

        # # generate the pairs 
        # for i in range(len(nums)//2):
        #     final_ans += min(nums[i*2], nums[i*2+1])

        # # get the maximized sum
        # return final_ans 

        nums.sort()
        return sum(nums[::2])
