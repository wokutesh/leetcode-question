class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        res=[]
        for passengers,start,end in trips:
            res.append((start,passengers))
            res.append((end,-passengers))

        res.sort()
        count=0
        for i,passes in res:
            count+=passes
            if count>capacity:
                return False
        return True
