class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        nums.sort()
        ans=[]
        for j in range(len(nums)-1,-1,-1):
            ans.append(nums[j])
            if sum(ans) > sum(nums[:j]):
                break
        
        return ans
        