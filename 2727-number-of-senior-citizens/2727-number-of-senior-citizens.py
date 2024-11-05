class Solution:
    def countSeniors(self, details: List[str]) -> int:
        
        count=0
        for person in details:
            x=person[11:13]
            if int(x)>60:
                count+=1
        
        return count

      

        