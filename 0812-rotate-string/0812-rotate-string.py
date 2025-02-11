class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
       
       
        if len(s)!=len(goal):
            return False
        
        dq=deque(s)
        for _ in range(len(s)):
            dq.rotate(-1)
            if ''.join(dq)==goal:
                return True
        return False
