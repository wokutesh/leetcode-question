class Solution:
    def sumZero(self, n: int) -> List[int]:
        res=[i for i in range(1,n)]
        res.append(-1 * sum(res))
        return res
    
      



        