class Solution:
    def numberOfPoints(self, nums: List[List[int]]) -> int:
        
        unique_vals = []
       
        for i,elements in enumerate(nums):
            start, end = elements
            for i in range(start,end+1):
                unique_vals.append(i)

        return len(set(unique_vals))

        