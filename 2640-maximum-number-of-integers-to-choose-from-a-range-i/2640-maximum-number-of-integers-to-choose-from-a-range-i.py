class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        ans = []
        curr_diff = 0
        banned=set(banned)
        for i in range(1, n+1):

            if i not in banned :
                if curr_diff + i <=maxSum:
                    
                    curr_diff+=i
                    ans.append(i)
                else:
                    break
        return len(ans)
