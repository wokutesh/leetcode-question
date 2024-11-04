class Solution:
    def minSteps(self, s: str, t: str) -> int:
        s_counts = Counter(s)
        t_counts = Counter(t)
        count = 0
        
        for char, t_count in t_counts.items():
            s_count = s_counts.get(char, 0)
            if t_count > s_count:
                count += t_count - s_count 
            elif s_count == 0:
                count += t_count  
        
        return count

        