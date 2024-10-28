class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        total=[]
        for i in range(len(nums)):
            left=0
            for j in range(len(nums)):
                if j<=i:
                    left+=nums[j]
            total.append(left)
        return total
        