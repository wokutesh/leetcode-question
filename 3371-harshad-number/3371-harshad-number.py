class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        res=[int(y) for y in str(x)]
        sum_=sum(res)
        if x%sum_==0:
            return sum_
        return -1
        