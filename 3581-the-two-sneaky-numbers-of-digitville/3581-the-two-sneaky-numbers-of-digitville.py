
class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
    
        num1=[]
        for i in range(len(nums)):
            if nums.count(nums[i])>1:
                num1.append(nums[i])
        l=list(set(num1))
        return l               
            
        
        
        


        