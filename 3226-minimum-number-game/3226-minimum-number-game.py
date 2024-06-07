class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        # sort the array 
        # append bob num then append alice num
        nums.sort()

        # result arr 
        arr = []
        for i in range(len(nums)):
            if i % 2 != 0:
                bob = nums[i]
            else:
                continue
            # bob = nums[i] if i % 2 != 0 else continue
            alice = nums[i-1]
            arr.append(bob)
            arr.append(alice)
        return arr