class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:

        heap = []
        for i, val in enumerate(classes):
            a, b = val
            j = (a/b)-(a+1)/(b+1)
            heapq.heappush(heap, (j, i))
        
        while extraStudents > 0:
            j, i = heapq.heappop(heap)
            a, b = classes[i]
            classes[i]=[a+1, b+1]
            j = ((a+1)/(b+1))-((a+2)/(b+2))
            heapq.heappush(heap, (j, i))
            extraStudents-=1
        
        res = 0
        for i, val in enumerate(classes):
            a,b = val
            res+=a/b

        res=res/len(classes)
        return res        
