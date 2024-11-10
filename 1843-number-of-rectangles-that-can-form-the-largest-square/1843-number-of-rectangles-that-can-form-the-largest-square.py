class Solution:
    def countGoodRectangles(self, rectangles: List[List[int]]) -> int:
        count=0
        mx=0
        for ele in rectangles:
            mn=min(ele)
            if mn>mx:

                mx=mn
                count=1
            elif mx==mn:
                count+=1
        return count

        