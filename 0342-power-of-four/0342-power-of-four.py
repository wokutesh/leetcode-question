class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        def is_power(n):

            if n <= 0:
                return False
            if n == 1:
                return True
            if n % 4 != 0:
                return False
            return is_power(n//4)
        
        return is_power(n)