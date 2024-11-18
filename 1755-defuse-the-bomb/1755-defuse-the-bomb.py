class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        ans = []

        n = len(code)

        if k > 0:  
            for i in range(n):
                ans.append(sum(code[(i + 1 + j) % n] for j in range(k)))
        elif k < 0:  
            for i in range(n):
                ans.append(sum(code[(i - 1 - j) % n] for j in range(-k)))
        else: 
            ans = [0] * n

        return ans
        