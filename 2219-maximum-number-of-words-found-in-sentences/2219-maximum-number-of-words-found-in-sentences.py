class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        res=[]
        for i in range(len(sentences)):
            res.append(len(sentences[i].split()))
        return max(res)
        