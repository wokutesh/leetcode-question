class Solution:
    def isBalanced(self, num: str) -> bool:
        res=[int(x) for x in num]
        even_sum=0
        odd_sum=0
        for i in range(len(res)):
            if i%2==0:
                even_sum+=res[i]
            else:
                odd_sum+=res[i]

        return even_sum==odd_sum
        