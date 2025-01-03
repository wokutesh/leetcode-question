class Solution:
    def findTheArrayConcVal(self, nums: List[int]) -> int:
        val=0
        i,j=0,len(nums)-1

        while i<=j:
            if i==j:
                val+=nums[i]
            else:

                string=''
                string+=str(nums[i])
                string+=str(nums[j])
                val+=int(string)    
        
            i+=1
            j-=1

        return val