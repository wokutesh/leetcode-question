class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        q1=[]
        for i in range(len(l)):
            sub_a=nums[l[i]:r[i]+1]
            sub_a.sort()
            arth=True
            diff=sub_a[1]-sub_a[0]

            for j in range(1,len(sub_a)-1):
                if sub_a[j+1]-sub_a[j]!=diff:
                    arth=False
            q1.append(arth)
        return q1
                

        