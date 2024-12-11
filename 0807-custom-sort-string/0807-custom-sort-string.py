class Solution:
    def customSortString(self, order: str, s: str) -> str:
        s_count = Counter(s)

    
        result = []

      
        for char in order:
            if char in s_count:
                result.append(char * s_count[char]) 
                del s_count[char]  

     
        for char in s:
            if char in s_count: 
                result.append(char * s_count[char])
                del s_count[char]  

        return ''.join(result)