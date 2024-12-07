class Solution:
    def minOperations(self, logs: List[str]) -> int:
        count=0
        for idx in logs:
            if idx=='./':
                continue
            elif idx=='../':
                if count>0:
                    count-=1
            else:
                count+=1
        return count
        