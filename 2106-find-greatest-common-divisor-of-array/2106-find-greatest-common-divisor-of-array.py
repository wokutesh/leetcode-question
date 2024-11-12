class Solution:
    def findGCD(self, nums: List[int]) -> int:
        ans=[]
        for i in range(1,max(nums)+1):
            if max(nums)%i==0 and min(nums)%i==0:
                ans.append(i)

        return max(ans)

        