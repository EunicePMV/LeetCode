class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        # target arr is empty
        # index[i] -> index value, to be insert nums[i]
        target = []
        for i in range(len(index)):
            target.insert(index[i], nums[i])
        return target
