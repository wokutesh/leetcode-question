class Solution:
    def smallestEqual(self, nums: List[int]) -> int:
        ans=[]
        for i in range(len(nums)):
            if i%10==nums[i]:
                ans.append(i)
        if ans:
            return min(ans)
        return -1
        