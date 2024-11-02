class Solution:
    def canAliceWin(self, nums: List[int]) -> bool:
        double=0
        single=0
        for i in range(len(nums)):
            if nums[i]>=10:
                double+=nums[i]

            else:
                single+=nums[i]

        return single!=double

        