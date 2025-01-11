class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        if len(s)<k:
            return False
        
        count_char=Counter(s)
        count=0
        for key,val in count_char.items():
            if val % 2!=0:
                count+=1

        if count>k:
            return False
        else:
            return True
