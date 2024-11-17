class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        n=len(nums)
        pq=[]
        cs=0
        res=math.inf
        for i in range(n):
            cs+=nums[i]
            if cs>=k:
                res=min(res,i+1)
          
            while pq and cs-pq[0][0]>=k:
                res=min(res,i-heappop(pq)[1])
            heappush(pq,[cs,i])
        return res if res!=math.inf else -1
                


        

        