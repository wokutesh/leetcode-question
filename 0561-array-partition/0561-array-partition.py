class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        sum_=0
        for i in range(0,len(nums)-1,2):
            sum_+=min(nums[i],nums[i+1])

        return sum_
