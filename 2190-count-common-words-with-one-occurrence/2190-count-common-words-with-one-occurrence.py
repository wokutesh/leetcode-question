class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        count1=Counter(words1)
        count2=Counter(words2)
        count=0
        for word in words1:
            if count1[word]==1 and count1[word]==count2[word]:
                count+=1

        return count