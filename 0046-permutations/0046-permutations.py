class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res=[list(x) for x in permutations(nums)]
        return res
        