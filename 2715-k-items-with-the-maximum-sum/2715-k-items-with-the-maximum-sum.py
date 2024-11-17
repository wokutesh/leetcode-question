class Solution:
    def kItemsWithMaximumSum(self, numOnes: int, numZeros: int, numNegOnes: int, k: int) -> int:
        count=0
        one=[1]*numOnes
        zero=[0]*numZeros
        neg=[-1]*numNegOnes
        total_list=one+zero+neg
        for i in range(k):
            count+=total_list[i]
        return count
        