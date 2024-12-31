class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        def is_prime(n):
            if n<=1:
                return False
            if n<=3:
                return True
            if n%2==0:
                return False
            
            for i in range(3,int(n**0.5)+1,2):
                if n%i==0:
                    return False
            return True
        count=0
        for i in range(left,right+1):
            binary=bin(i)[2:]

            ones=binary.count('1')
            if is_prime(ones):
                count+=1
        return count