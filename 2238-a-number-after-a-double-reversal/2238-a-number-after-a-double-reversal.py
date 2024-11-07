class Solution:
    def isSameAfterReversals(self, num: int) -> bool:
        str1=num
        r1=str(num)
        r2=int(r1[::-1])
        r3=str(r2)
        r4=int(r3[::-1])
        
        return r4==str1
        
       
                
            
    
        