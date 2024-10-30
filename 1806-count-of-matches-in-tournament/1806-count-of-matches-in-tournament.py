class Solution:
    def numberOfMatches(self, n: int) -> int:
        total=0
        while n>1:
            total+=n//2
            n=ceil(n/2)

            
        return total


        