class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        res = [idx for idx, i in enumerate(s) if i == c]
        ans = []
        for idx, i in enumerate(s):
            min_distance = float('inf') 
            for num in res:
                distance = abs(idx - num)  
                min_distance = min(min_distance, distance)  
            ans.append(min_distance) 
        return ans
            