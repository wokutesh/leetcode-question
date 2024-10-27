class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        res=[i for i,j in points]
        res.sort()
        result=[]
        for i in range(len(res)-1):
            result.append(res[i+1]-res[i])
        return max(result)
        