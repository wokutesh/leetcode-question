class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        
        res= [(name, height) for name, height in zip(names, heights)]

        res.sort(key=lambda item:item[1],reverse=True)
        result=[]
        for  i in res:
            result.append(i[0])
        return result


        