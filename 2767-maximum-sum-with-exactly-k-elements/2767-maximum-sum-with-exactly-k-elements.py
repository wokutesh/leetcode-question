class Solution:
    def maximizeSum(self, nums: List[int], k: int) -> int:
        res=0
        for i in range(k):
            mx=max(nums)
            res+=mx
            
            nums[-1]=mx+1

        return res
            

        