class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        ans = []
        for i in range(left, right + 1):
            str_i = str(i)
            is_divide = True
            
            for char in str_i:
                digit = int(char)
                
                if digit == 0 or i % digit != 0:
                    is_divide = False
                    break
                    
            if is_divide:
                ans.append(i)
        
        return ans
            
                
        