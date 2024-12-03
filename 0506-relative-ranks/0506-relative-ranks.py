class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        if len(score) == 1:
            return ["Gold Medal"]
    
   
        score_sorted = sorted(enumerate(score), key=lambda x: -x[1])
        
    
        res = [None] * len(score)

        for i, (idx, val) in enumerate(score_sorted):
            if i == 0:
                res[idx] = "Gold Medal"
            elif i == 1:
                res[idx] = "Silver Medal"
            elif i == 2:
                res[idx] = "Bronze Medal"
            else:
                res[idx] = str(i + 1)
        
        return res


            