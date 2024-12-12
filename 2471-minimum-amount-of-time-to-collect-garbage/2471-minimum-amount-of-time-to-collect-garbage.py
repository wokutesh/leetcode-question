class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
    
        total_time = 0
    
      
        last_glass = last_paper = last_metal = 0

        for i, g in enumerate(garbage):
            
            total_time += len(g)
            
          
            if 'G' in g:
                last_glass = i
            if 'P' in g:
                last_paper = i
            if 'M' in g:
                last_metal = i
        
        
        total_time += sum(travel[i] for i in range(last_glass))
        total_time += sum(travel[i] for i in range(last_paper))
        total_time += sum(travel[i] for i in range(last_metal))
        
        return total_time