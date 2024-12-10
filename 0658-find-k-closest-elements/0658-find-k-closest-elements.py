class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
       
        i = 0
        j = len(arr) - 1

    
        while j - i >= k:
           
            if abs(arr[i] - x) > abs(arr[j] - x):
                i += 1  
            else:
                j -= 1 

        
        ans = arr[i:j + 1]
        return ans