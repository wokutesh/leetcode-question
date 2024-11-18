class Solution:
    def generateKey(self, num1: int, num2: int, num3: int) -> int:
        ans1=['0']*(4-len(str(num1)))+list(str(num1))
        ans2=['0']*(4-len(str(num2)))+list(str(num2))
        ans3=['0']*(4-len(str(num3)))+list(str(num3))
        s=''
        for i in range(4):
            s+=min(ans1[i],ans2[i],ans3[i])

        return int(s)

        


        