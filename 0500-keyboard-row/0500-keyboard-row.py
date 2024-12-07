class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        ans=[]
        row1="qwertyuiop"
        row2="asdfghjkl"
        row3="zxcvbnm"
        for word in words:
            lower=word.lower()
            if all(i in row1 for i in lower ):
                ans.append(word)
            elif all(i in row2 for i in lower):
                ans.append(word)
            elif all(i in row3 for i in lower):
                ans.append(word)

        return ans