class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        count = 1
        nums.sort()  
        ans = nums[0]   

        for num in nums:  
           
            if num-ans > k:
                count += 1
                ans = num 

        return count
            