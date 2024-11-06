class Solution:
    def minimumChairs(self, s: str) -> int:
        Ans=Chairs=0
        for i in range(len(s)):
            if s[i]=='E':
                Chairs+=1
            elif s[i]=='L':
                Chairs-=1

            Ans=max(Ans,Chairs)
        return Ans




        