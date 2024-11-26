class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
       
        return sum(1 for i in range(limit+1) for j in range(limit+1) for k in range(limit+1) if i+j+k==n)
        