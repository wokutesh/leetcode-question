class Solution:
    def countSubstrings(self, s: str) -> int:
        count=0
        for i in range(len(s)):
            for j in range(i+1,len(s)+1):
                res=s[i:j]
            
                if res==res[::-1]:
                    count+=1


        return count