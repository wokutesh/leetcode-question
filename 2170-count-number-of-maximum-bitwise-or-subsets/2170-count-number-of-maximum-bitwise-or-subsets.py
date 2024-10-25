class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:

        maxOR = 0
        prevCnt = Counter()
        prevCnt[0] = 1
        curCnt = Counter()
        for x in nums:
            maxOR |= x
            for val, reps in prevCnt.items():
                curCnt[val | x] += reps
            prevCnt.update(curCnt)
            curCnt.clear()
        return prevCnt[maxOR]