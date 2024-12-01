class Solution:
    def occurrencesOfElement(self, nums: List[int], queries: List[int], x: int) -> List[int]:
    
        dict_count = {}
        count=0 

       
        for idx, val in enumerate(nums):
            if val == x:
                count+=1
                dict_count[count] = idx

        
        ans = []
        for query in queries:
          
            if query in dict_count:
                ans.append(dict_count[query])
            else:
                ans.append(-1)

        return ans

        return ans