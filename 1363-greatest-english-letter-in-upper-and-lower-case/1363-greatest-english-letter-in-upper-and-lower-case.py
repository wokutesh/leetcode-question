class Solution:
    def greatestLetter(self, s: str) -> str:
        if s is None:
            return ''
        s_set=set(s)
        great=''
        for i in s_set:
            if i.isupper() and i.lower() in s_set:
                great=max(great,i)
                
        

          
        return great
