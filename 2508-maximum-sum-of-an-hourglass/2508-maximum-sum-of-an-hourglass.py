class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:

        sum_=0
        for i in range(len(grid)-2):
            for j in range(len(grid[0])-2):
                top=grid[i][j]+grid[i][j+1]+grid[i][j+2]
                middle=grid[i+1][j+1]
                bottom=grid[i+2][j]+grid[i+2][j+1]+grid[i+2][j+2]
                sum_=max(sum_,top + middle + bottom)
                
        return sum_
        