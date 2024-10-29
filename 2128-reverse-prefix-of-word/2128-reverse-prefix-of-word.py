class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        for i in range(len(word)):

            if word[i]==ch:
                data=word[i+1:]
                info=word[:i+1]
                break
        else:
            return word
        infos=''.join(reversed(info))
        s=infos + data
        return s
                
        