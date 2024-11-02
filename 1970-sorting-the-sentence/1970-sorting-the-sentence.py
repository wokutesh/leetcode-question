class Solution:
    def sortSentence(self, s: str) -> str:

        words=s.split()

        res={int(word[-1]):word[:-1] for word in words}

        sorted_res=' '.join(value for key,value in sorted(res.items()))

        return sorted_res

        