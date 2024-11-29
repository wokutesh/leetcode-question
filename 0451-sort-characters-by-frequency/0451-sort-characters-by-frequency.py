class Solution:
    def frequencySort(self, s: str) -> str:
     

        count=Counter()
        for i in s:
            count[i]+=1

        res=''
        sorted_count=dict(sorted(count.items(),key=lambda x:x[1],reverse=True))
        for key,val in sorted_count.items():
            res+=key * val

        return res
        