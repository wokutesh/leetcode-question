class Solution:
    def balancedStringSplit(self, s: str) -> int:
        count=0
        i=0
        res=0
        for i in range(len(s)):
          
            if s[i]=='R':

                res+=1
            else:
                res-=1

            if res==0:
                count+=1
            
            
        return count

