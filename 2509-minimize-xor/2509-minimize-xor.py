class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        set2 = bin(num2).count("1")
        set1 = bin(num1).count("1")
        if set1 == set2:
            return num1
        diff = set1 - set2
        

        if diff < 0:
            while bin(num1).count("1") < set2:
                num1 |= (num1 + 1)
        if diff > 0:
            while bin(num1).count("1") > set2:
                num1 &= (num1 - 1)

        
        return num1