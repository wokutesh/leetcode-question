class Solution:
    def isStrictlyPalindromic(self, n: int) -> bool:
        if n<=2:
            return False
        for i in range(2,n-1):
            result=[]
            temp=n
            while temp>0:
                result.append(str(temp%i))
                temp//=i
            string=''.join(result)
            if string!=string[::-1]:
                return False


        return True
        