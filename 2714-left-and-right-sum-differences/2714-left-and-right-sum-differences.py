class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        
        total=[]
        

        for i in range(len(nums)):
            right=0
            left=0
            for j in range(len(nums)):
                if j<i:

                    left+=nums[j]
                elif j>i:
                    right+=nums[j]
            total.append(abs(left-right))
        return total
        



        