class Solution:
    def returnToBoundaryCount(self, nums: List[int]) -> int:
        res=list(accumulate(nums))
        return res.count(0)
        