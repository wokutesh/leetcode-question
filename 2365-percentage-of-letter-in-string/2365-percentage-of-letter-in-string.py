class Solution:
    def percentageLetter(self, s: str, letter: str) -> int:
        percentage=(s.count(letter)/len(s))*100
        return floor(percentage)
        