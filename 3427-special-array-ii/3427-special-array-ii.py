class Solution:
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:

        n = len(nums)
        
       
        special_prefix = [0] * n
        for i in range(n - 1):
            if (nums[i] % 2) != (nums[i + 1] % 2):  
                special_prefix[i + 1] = 1
        
      
        for i in range(1, n):
            special_prefix[i] += special_prefix[i - 1]
        
    
        result = []
        for start, end in queries:
            if end - start == 0:  
                result.append(True)
                continue
            
            
            count_special = special_prefix[end] - (special_prefix[start] if start > 0 else 0)
            result.append(count_special == (end - start))
        
        return result