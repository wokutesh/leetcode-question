class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        res=[0]
        result=[]
        tot=0
        for i in range(len(gain)):
            tot+=gain[i]
            result.append(tot)
        return max(res + result)

        