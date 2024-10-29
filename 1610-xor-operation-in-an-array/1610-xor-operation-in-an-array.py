class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        res=0
        result=[]
        for i in range(n):
            result.append(start + 2*i)
        for element in result:
            res^=element
        return res
        