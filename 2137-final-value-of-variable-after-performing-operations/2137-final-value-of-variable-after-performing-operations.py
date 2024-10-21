class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:

        sum =0
        for i in range(len(operations)):
            if operations[i]=='X++':
                sum+=1
            elif  operations[i]=='++X':
                sum+=1
            elif  operations[i]== 'X--':
                sum-=1
            elif  operations[i]=='--X':
                sum-=1
            else:
                sum=0
        return sum 

        