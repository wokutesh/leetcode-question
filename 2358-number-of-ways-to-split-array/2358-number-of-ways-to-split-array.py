class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        count=0
        left_sum=0
        total=sum(nums)
        for i in range(len(nums)-1):
            left_sum+=nums[i]
            remainder=total-left_sum
            if left_sum>=remainder:
                count+=1
            

        return count
        