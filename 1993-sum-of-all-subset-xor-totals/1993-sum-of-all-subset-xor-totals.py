class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        res=[[]]
        sum=0
      
        for num in nums:
            res +=[curr + [num] for curr in res]
        for j in res:
            x_or=0
            for i in range(len(j)):
                x_or ^=j[i]
            sum+=x_or
        return sum


        