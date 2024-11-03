class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        count=0
        for i in range(len(nums)):
            for j in range(i+1,len(nums)+1):
                subarray=nums[i:j]
                sub_set=set(subarray)
                count+=(len(sub_set))**2

        return count

        