class Solution:
    def countDigits(self, num: int) -> int:
        res=[int(x) for x in str(num)]
        count=0
        for i in range(len(res)):
            if num%res[i]==0:
                count+=1
        return count
        