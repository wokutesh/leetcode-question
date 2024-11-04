class Solution:
    def makeSmallestPalindrome(self, s: str) -> str:
        s=list(s)
        for i in range(len(s)//2):
            c=min(s[i],s[~i])
            s[i],s[~i]=c,c
        return ''.join(s)
        