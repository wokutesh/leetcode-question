class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        res=[]
        count=Counter(nums)

        for ind,val in count.items():
            if val>1:
                res.append(ind)

        return res
        