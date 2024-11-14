class Solution:
    def calPoints(self, operations: List[str]) -> int:
        ans=[]
        for oper in operations:
            if oper =='C':
                if ans:

                    ans.pop()
            elif oper=='D':

                if ans:
                    ans.append(ans[-1]*2)
            elif oper=='+':
                if len(ans)>=2:
                    ans.append(ans[-1]+ans[-2])

            else:
                ans.append(int(oper))

        return sum(ans)



        