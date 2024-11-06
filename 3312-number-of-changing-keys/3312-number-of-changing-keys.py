class Solution:
    def countKeyChanges(self, s: str) -> int:
        count=0
        str1=s.lower()
        for i in range(len(str1)-1):
            if str1[i]!=str1[i+1]:
                count+=1
        
        return count
        