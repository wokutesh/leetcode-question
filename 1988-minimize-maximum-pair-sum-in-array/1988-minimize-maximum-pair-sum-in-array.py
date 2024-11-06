class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        res=[]
        nums.sort()
        l=0
        r=len(nums)-1

        while l<r:
            res.append(nums[l]+nums[r])
            l+=1
            r-=1
        return max(res)



   
        