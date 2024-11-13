class Solution:
    def partitionString(self, s: str) -> int:
        str1=''
        res=[]
        for i in range(len(s)):
            if s[i] not in str1:
                str1+=s[i]
            else:
                res.append(str1)
                str1=''
                str1+=s[i]
        res.append(str1)
        return len(res)


        

        