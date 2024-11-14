class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        res={}
        ans=[]
        for i in range(len(arr)):
            if arr[i] in res:
                res[arr[i]]+=1
            else:
                res[arr[i]]=1

        for key,val in res.items():
            ans.append(val)

        return len(ans)==len(set(ans))