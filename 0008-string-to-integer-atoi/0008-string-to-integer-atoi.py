class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip() 
        if not s:
            return 0  

        sign = 1
        i = 0

       
        if s[0] == '-':
            sign = -1
            i += 1
        elif s[0] == '+':
            i += 1

        num = 0
        while i < len(s) and s[i].isdigit():
            num = num * 10 + int(s[i])
            i += 1

      
        num *= sign

       
        num = max(-2**31, min(num, 2**31 - 1))

        return num