class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        if len(nums)==1:
            return True
        ans=[]
        for i in range(len(nums)-1):
            if (nums[i+1] + nums[i])%2==0:
                return False
                break
        return True

        