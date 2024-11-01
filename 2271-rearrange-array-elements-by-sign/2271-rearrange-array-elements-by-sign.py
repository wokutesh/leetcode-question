class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        pos=[]
        neg=[]
        result=[]
        for i in range(len(nums)):
            if nums[i]>0:
                pos.append(nums[i])
            elif nums[i]<0:
                neg.append(nums[i])

        for x,y in zip(pos,neg):
            result+=[x,y]
        return result
        