class Solution:
    def repeatedCharacter(self, s: str) -> str:
        count=Counter()
        for i in range(len(s)):
            count[s[i]]+=1
         
            if count[s[i]]==2:
                return s[i]
                break

        