class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        ans=[]
        if len(nums)==1:
            ans.append(0)
            ans.append(len(nums))

        count=0
        i=0
        nums.sort()
        while i<len(nums)-1:
            
            if nums[i]==nums[i+1]:
                
                
                del nums[i+1]
                del nums[i]
                count+=1
            else:
                i+=1
      
        return [count,len(nums)]
                    

