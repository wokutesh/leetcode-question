class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
      
        stack = [values[0]]
        best = 0
        for index, x in enumerate(values):
            if index == 0:
                continue

            score = -index + x
            best = max(best, stack[-1] + score)
            
            score = index + x
            while stack and stack[-1] < score:
                stack.pop()

            if not stack:
                stack.append(score)

        return best
            
        

        