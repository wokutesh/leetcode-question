class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        
        
        if len(set(nums)) < k: 
            return 0

        max_sum = 0
        current_sum = 0
        window = set()
        left = 0

        for right in range(len(nums)):
            
            while nums[right] in window or len(window) >= k:
                window.remove(nums[left])
                current_sum -= nums[left]
                left += 1

            window.add(nums[right])
            current_sum += nums[right]

        
            if len(window) == k:
                max_sum = max(max_sum, current_sum)

        return max_sum
            
                

            