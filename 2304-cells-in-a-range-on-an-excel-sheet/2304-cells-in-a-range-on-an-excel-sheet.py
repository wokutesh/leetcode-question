class Solution:
    def cellsInRange(self, s: str) -> List[str]:
        a,b=s.split(':')

        col1,row1=ord(a[0]),int(a[1])
        col2,row2=ord(b[0]),int(b[1])
        res=[]
        for i in range(col1,col2+1):
            for  j in range(row1,row2+1):
                res.append(chr(i)+str(j))
        return res


        