class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        count=0
        for element in items:
            if ruleKey=='color':
                if ruleValue==element[1]:
                    count+=1
            elif ruleKey=='type':
                if ruleValue==element[0]:
                    count+=1
            elif ruleKey=='name':
                if ruleValue==element[2]:
                    count+=1
        return count


        