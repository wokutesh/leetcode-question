class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        res=[]
        for i in range(len(nums)):
            num_str=str(nums[i])
            num_reversed=int(num_str[::-1])
            res.append(num_reversed)

        return len(set(nums + res))

        