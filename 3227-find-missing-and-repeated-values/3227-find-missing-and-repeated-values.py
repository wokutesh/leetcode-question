class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        total = 0
        
        for i in range(len(grid)**2,0,-1):
            total += i
        
        dict_ = {}
        
        to_set = set(x for row in grid for x in row)
        
       
        b = (total ) - sum(to_set)  
        ans = []
        
       
        for row1 in grid:
            for j in range(len(row1)):
                if row1[j] in dict_:
                    dict_[row1[j]] += 1
                else:
                    dict_[row1[j]] = 1
        
      
        for key, val in dict_.items():
            if val == 2:
                ans.append(key)
        
   
        ans.append(b)
        
        return ans


