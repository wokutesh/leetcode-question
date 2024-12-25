class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        res = []
        sorted_nums=sorted(nums)
        for i in range(0, len(nums), 3):
            temp = sorted_nums[i:i+3]  
            if max(temp)-temp[0]<=k:
                res.append(temp)

        if len(res)==len(nums)//3:
            return res
        else:
            return []
        


        