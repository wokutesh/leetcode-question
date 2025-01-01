class Solution:
    def maxScore(self, s: str) -> int:
        max_score=0
        for i in range(len(s)-1):
            left=s[:i+1]
            right=s[i+1:]
            
            left_score=left.count('0')
         
            right_score=right.count('1')
            score=left_score +right_score
            max_score=max(max_score,score)
        return max_score
        