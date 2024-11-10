class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        i=0
        n=len(s)
        res=[]
        for c in s:
            if c=='I':
                res.append(i)
                i+=1
            else:
                res.append(n)
                n-=1
        res.append(i)
        return res


        

        