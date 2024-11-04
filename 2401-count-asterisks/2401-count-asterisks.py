class Solution:
    def countAsterisks(self, s: str) -> int:
        count=0
        cq=0

        for i in s:
            if i=='|':
                cq+=1
            elif i=='*' and cq%2==0:
                count+=1
        return count
        
                
                
            
               
                   

    
        