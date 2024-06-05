class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        points.sort()
        max_vertical = 0
        for i in range(1, len(points)-1):
            n = points[i][0] - points[i-1][0]
            max_vertical = n if max_vertical < n else max_vertical
        return max_vertical

        