class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        count=Counter()
        for i in range(len(nums)):
        
            count[nums[i]]+=1

        if all(val %2==0 for val in count.values()):
            return True
        return False
        