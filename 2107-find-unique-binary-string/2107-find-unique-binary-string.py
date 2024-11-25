class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        n=len(nums)
        res=[bin(i)[2:].zfill(n) for i in range(2**n)]
        for j in res:
            if j not in nums:
                return j
                break


        