class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        res=[]
        for i in range(k):
            mn=min(nums)
            nums[nums.index(mn)]=mn*multiplier

        return nums

        