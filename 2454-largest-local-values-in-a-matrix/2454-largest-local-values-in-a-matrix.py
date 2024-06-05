class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        # get the ans dimension
        n = len(grid)

        # initialize the answer with the correct dimension
        ans = [[0] * (n-2) for _ in range(n-2)]

        # iterate through the dimension
        for i in range(n-2):
            for j in range(n-2):
                temp = []
                for col in range(i, i+3):
                    for row in range(j, j+3):
                        temp.append(grid[col][row])
                ans[i][j] = max(temp)
        return ans