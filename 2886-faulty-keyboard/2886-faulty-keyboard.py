class Solution:
    def finalString(self, s: str) -> str:
        s_reverse=[]
        for i in s:
        
            if i!='i':
                s_reverse.append(i)
                
            else:
                s_reverse=s_reverse[::-1]

        return ''.join(s_reverse)
