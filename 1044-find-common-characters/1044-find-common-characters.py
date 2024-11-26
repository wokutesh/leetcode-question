class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        common={i:words[0].count(i) for i in words[0]}

        for i in range(1,len(words)):
            for j in common:
                if j in words[i]:
                    common[j]=min(common[j],words[i].count(j)) 
                else:
                    common[j]=0

        res=[]
        for i in common:
            res+=i*common[i]
        return res  

      


       
        