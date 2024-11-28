class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        count=0
        total=0
       
        for i in range(len(costs)):
            
            if total + costs[i] <=coins:
                total+=costs[i]
                count+=1
                
            else:
                break
        return count