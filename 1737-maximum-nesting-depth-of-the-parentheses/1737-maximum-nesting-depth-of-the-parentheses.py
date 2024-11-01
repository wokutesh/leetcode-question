class Solution:
    def maxDepth(self, s: str) -> int:
        curr=0
        max_curr=0

        for i in s:
            if i=='(':
                curr+=1
                max_curr=max(max_curr,curr)
            elif i==')':
                curr-=1

        return max_curr        