class Solution:
    def minElement(self, nums: List[int]) -> int:
        result=[]
        for element in nums:
            ele_str=str(element)
            res=[int(x) for x in ele_str]
            total=sum(res)

            result.append(total)
        return min(result)