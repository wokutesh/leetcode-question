class Solution:
    def sumBase(self, n: int, k: int) -> int:
        if n==0:
            return 0
        count=0
        while n>0:
            rem=n%k
            count+=rem
            
            n//=k

        return count