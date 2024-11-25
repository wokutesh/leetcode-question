class Solution:
    def splitWordsBySeparator(self, words: List[str], separator: str) -> List[str]:
        ans=[]
        for row in words:
           ans.extend(i for i in row.split(separator) if i)
              

        return ans 