class Solution:
    def findingUsersActiveMinutes(self, logs: List[List[int]], k: int) -> List[int]:

        ans=[0]*k
        res=defaultdict(set)

        for id,time in logs:
            res[id].add(time)
        
        for time in res.values():
            if len(time)<=k:
                ans[len(time)-1]+=1

        return ans