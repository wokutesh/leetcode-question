class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        num=[]
        for i in s.split():
            if i.isdigit():
                num.append(int(i))
        
        for j in range(len(num)-1):
            if num[j]>=num[j+1]:
                return False
                break

        return True
                


          