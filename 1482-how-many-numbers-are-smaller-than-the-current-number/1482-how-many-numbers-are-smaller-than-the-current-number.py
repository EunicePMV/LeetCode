class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        # declare list to to be return
        greater_value_counter = []
        # loop throughout the input list
        for i in range(len(nums)):
            count = 0
            # with the first element, compare to the next element, starting to the i+1 index position
            for j in range(len(nums)):
                if j == i:
                    continue
                elif nums[i] > nums[j]:
                    count += 1
            greater_value_counter.append(count)
        return greater_value_counter 