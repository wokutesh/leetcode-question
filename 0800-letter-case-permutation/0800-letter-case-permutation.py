class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        ans=['']
        for c in s:
            tmp = []
            for o in ans:
                tmp.append(o + c)
                if c.isalpha():
                    tmp.append(o + c.swapcase())
            ans = tmp

        return ans