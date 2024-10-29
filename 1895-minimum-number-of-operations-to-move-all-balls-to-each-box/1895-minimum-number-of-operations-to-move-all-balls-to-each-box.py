class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        final=[]

        for i in range(len(boxes)):
            left=[i-x for x in range(0,i) if boxes[x]=='1']
            right=[x-i for x in range(i+1,len(boxes)) if boxes[x]=='1']
            final.append(sum(left+right))
        return final
        