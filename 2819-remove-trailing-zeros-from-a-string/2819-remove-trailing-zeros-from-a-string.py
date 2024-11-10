class Solution:
    def removeTrailingZeros(self, num: str) -> str:
        num_str=int(num[::-1])
        num1=str(num_str)
        return num1[::-1]
        