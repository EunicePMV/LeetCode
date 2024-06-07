class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        ans = [i for i in nums if i < k]
        return len(ans)
