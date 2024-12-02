class Solution:
    def hammingWeight(self, n: int) -> int:
        binary_num=bin(n)
        return binary_num.count('1')
        