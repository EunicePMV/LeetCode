class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        x_axis = []
        for point in points:
            x_axis.append(point[0])

        plot_points = sorted(x_axis)
        wide_vertical = 0
        for i, point in enumerate(plot_points):
            if i != len(plot_points)-1:
                n = plot_points[i+1] - point
                if n > wide_vertical:
                    wide_vertical = n
        return wide_vertical
        