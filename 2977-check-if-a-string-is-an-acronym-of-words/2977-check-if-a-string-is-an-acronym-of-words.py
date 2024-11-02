class Solution:
    def isAcronym(self, words: List[str], s: str) -> bool:
        s_=''
        for element in words:
            s_+=element[0]

        return s_==s


        