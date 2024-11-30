class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        count = Counter()
        winner_list =set() 
        
       
        for match in matches:
            winner, loser = match
             
            winner_list.add(winner)
            count[loser] += 1

        ans = [win for win in winner_list if win not in count]
        res = [key for key, val in count.items() if val == 1]  
        res.sort()
        ans.sort()
        return [ans, res]