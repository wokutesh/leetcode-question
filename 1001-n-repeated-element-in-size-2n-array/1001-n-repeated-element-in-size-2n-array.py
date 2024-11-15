class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        n=len(nums)//2
        ans={}
        for ele in nums:
            if ele in ans:
                ans[ele]+=1
            else:
                ans[ele]=1

        for key,val in ans.items():
            if val==n:
                return key