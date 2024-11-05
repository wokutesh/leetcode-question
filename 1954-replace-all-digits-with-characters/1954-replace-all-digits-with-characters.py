class Solution:
    def replaceDigits(self, s: str) -> str:
        res=list(s)
        string='abcdefghijklmnopqrstuvwxyz'
        for i in range(1,len(res),2):
            replacement=string.find(res[i-1]) +int(res[i])
            res[i]=string[replacement]
           

        return ''.join(res)