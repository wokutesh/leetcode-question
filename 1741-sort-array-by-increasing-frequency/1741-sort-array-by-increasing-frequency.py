class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        res={}
        for i in nums:
            if i in res:
                res[i]+=1

            else:
                res[i]=1

        nums.sort(key=lambda x: (res[x], -x))
        return nums
        