class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        counts=defaultdict(int)
        
        for element in edges:
            for row in element:
                counts[row]+=1
        count=dict(counts)

        for value,key in count.items():
            if key==len(edges):
                return value
        return None

        