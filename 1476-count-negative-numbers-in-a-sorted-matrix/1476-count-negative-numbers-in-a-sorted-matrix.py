class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        count=[]
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j]<0:
                    count.append(grid[i][j])
        return len(count)
        