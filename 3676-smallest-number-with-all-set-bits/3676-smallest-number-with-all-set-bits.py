class Solution:
    def smallestNumber(self, n: int) -> int:
        curr = 1
        while curr < n:
            curr = curr * 2 + 1
        return curr