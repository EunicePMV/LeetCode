class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        pairs = 0 

        # nested loop to loop through the arr of nums 
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                # nums[i] == nums[j]
                if nums[i] == nums[j] and (i*j) % k == 0:
                    pairs += 1
        return pairs 