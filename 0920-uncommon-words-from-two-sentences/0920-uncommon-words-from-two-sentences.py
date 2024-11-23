class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        s_word=s1.split()
        s2_word=s2.split()
        s1_count=Counter(s_word)
        s2_count=Counter(s2_word)
        ans=[]
        
        for key1 ,val1 in s1_count.items():
            if val1==1 and key1 not in s2_count:
                ans.append(key1)
        for key2,val2 in s2_count.items():
            if val2==1 and key2 not in s1_count:
                ans.append(key2)
        return ans


       