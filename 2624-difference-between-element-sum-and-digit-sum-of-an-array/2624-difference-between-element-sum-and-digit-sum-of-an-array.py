class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        dig=''.join(str(x) for x in nums)
        dig_sum=0
        
        digit_list=[int(x) for x in dig]
        for i in range(len(digit_list)):
            dig_sum+=digit_list[i]

        res=abs(sum(nums)-dig_sum)
        return res
        

        