class Solution:
    def minSteps(self, s: str, t: str) -> int:
        count_s=Counter(s)
        count_t=Counter(t)
        count=0
        for key,val in count_s.items():
            count+=abs(val-count_t[key])
            
        for key,val in count_t.items():
            if key not in count_s:
                count+=abs(val-count_s[key])
        return count
