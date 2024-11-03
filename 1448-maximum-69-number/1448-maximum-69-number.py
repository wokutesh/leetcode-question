class Solution:
    def maximum69Number (self, num: int) -> int:
        res=[]

        num_str=str(num)

        for i in range(len(num_str)):

            modified=list(num_str)

            if num_str[i]=='6':
                modified[i]='9'

            elif num_str[i]=='9':
                modified[i]=='6'

            res.append(int(''.join(modified)))

        return max(res)
       