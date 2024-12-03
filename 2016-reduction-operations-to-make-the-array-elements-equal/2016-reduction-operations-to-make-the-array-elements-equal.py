class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        if len(set(nums))==1 and len(nums)<=1:
            return 0
        nums.sort(reverse=True)
        count=0
       
        for i in range(1, len(nums)):
            if nums[i] < nums[i - 1]:
                count += i
        return count

