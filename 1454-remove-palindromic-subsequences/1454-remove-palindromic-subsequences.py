class Solution:
    def removePalindromeSub(self, s: str) -> int:
        if s==s[::-1]:
            return 1
        
        n = len(s)
        
        for i in range(n//2):
            if s[i] != s[n-i-1]:
                return 2