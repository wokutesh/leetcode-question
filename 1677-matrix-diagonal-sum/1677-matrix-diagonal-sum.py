class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        res=0
        n=len(mat)
        for i in range(len(mat)):
            res+=mat[i][i]
            res+=mat[i][n-i-1]

        if len(mat)%2!=0:
            res-=mat[n//2][n//2]

        return res
            
        