class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        n=len(s)//2
        a=s[:n]
        b=s[n:]
        count1=0
        count2=0
        str1='aeiouAEIOU'
        for i in range(len(a)):
            if a[i] in str1:
                count1+=1
        
        for j in range(len(b)):
            if b[j] in str1:
                count2+=1
        return count1==count2
        