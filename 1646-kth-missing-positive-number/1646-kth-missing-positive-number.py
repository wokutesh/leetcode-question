class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        i=1
        count=0
        while i>0:
            if i not in arr:
                count+=1

            if count==k:
                return i 
                break
            i+=1
