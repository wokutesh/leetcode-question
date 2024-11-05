class Solution:
    def duplicateNumbersXOR(self, nums: List[int]) -> int:
        num_count=Counter(nums)
        res=0
        for key,value in num_count.items():
            
            if value==2:
                res^=key

        return res




        