class Solution:
    def findPrefixScore(self, nums: List[int]) -> List[int]:
        res=[]
        conver=0
        max_val=0
        
        for i in range(len(nums)):
            
            max_val=max(max_val,nums[i])
            conver+=nums[i]+max_val
            res.append(conver)

        return res
        