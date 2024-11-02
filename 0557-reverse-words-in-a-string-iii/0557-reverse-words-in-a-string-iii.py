class Solution:
    def reverseWords(self, s: str) -> str:
        result=''
        words=s.split()
        for element in words:
            
            result+=element[::-1]+' '

        return result.strip()
        