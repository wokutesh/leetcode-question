class Solution:
    def findScore(self, nums: List[int]) -> int:
        minHeap = [(value, idx) for idx, value in enumerate(nums)]
        heapq.heapify(minHeap)

        score = 0

        while minHeap:
            value, idx = heapq.heappop(minHeap)

           
            if nums[idx] != -1:
                score += value
                nums[idx] = -1 

              
                if idx > 0:
                    nums[idx - 1] = -1
                if idx < len(nums) - 1:
                    nums[idx + 1] = -1

        return score


            
            