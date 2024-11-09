class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        res=[]
        for i in range(len(nums)):
            num_str=str(nums[i])
            for j in range(len(num_str)):
                res.append(int(num_str[j]))

        return res
        