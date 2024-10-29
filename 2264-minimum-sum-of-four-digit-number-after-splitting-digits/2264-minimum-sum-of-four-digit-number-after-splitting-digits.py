class Solution:
    def minimumSum(self, num: int) -> int:
        data=sorted(str(num))

        return int(data[0]+data[2])+ int(data[1]+data[3])
        