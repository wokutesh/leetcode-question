class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)-1):
            if nums[i]==nums[i+1]:
                nums[i]=nums[i]*2
                nums[i+1]=0
            else:
                continue

        last=[]
        for j in range(len(nums)):
            if nums[j]!=0:
                last.append(nums[j])
                
        return last + [0]*(len(nums)- len(last))