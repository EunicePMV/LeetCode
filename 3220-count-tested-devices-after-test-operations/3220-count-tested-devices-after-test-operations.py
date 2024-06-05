class Solution:
    def countTestedDevices(self, batteryPercentages: List[int]) -> int:
        ans = 0
        for n in batteryPercentages:
            if n - ans > 0:
                ans += 1
        return ans