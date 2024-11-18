class Solution:
    def removeStars(self, s: str) -> str:
        stack = []

        # loop 
        for c in s:
            if c == '*':
                stack and stack.pop()
            else:
                stack.append(c)

        return "".join(stack)
        