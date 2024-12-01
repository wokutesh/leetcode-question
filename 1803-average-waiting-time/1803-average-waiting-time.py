class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        
        ans=0
        free=0
        for arrive,time in customers:
            
            free=max(free,arrive) + time
            ans+=free- arrive

        return ans/len(customers)


        