class Solution:
    def sumIndicesWithKSetBits(self, nums: List[int], k: int) -> int:
     
        total=0
        for i in range(len(nums)):
            bin_count=bin(i).count('1')
            if bin_count==k:
                
                total+=nums[i]
        return total

        