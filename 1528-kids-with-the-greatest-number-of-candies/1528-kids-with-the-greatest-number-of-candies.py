class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max1=max(candies)
        res=[]
        for i in range(len(candies)):
            candy=candies[i]+ extraCandies
            
            res.append(candy>=max1)
           
        return res