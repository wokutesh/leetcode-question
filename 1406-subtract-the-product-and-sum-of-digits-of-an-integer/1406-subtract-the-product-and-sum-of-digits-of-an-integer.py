class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        add_res=0
        product=1
        res=[int(digit) for digit in str(n)]
        for i in range(len(res)):
            product*=res[i]
            add_res+=res[i]
        return product - add_res

        