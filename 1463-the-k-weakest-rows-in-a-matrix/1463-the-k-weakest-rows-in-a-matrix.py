class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        ans=[]
        count={}
        for idx,soldiers in enumerate(mat):
            count[idx]=soldiers.count(1)

        count_sorted=dict(sorted(count.items(), key=lambda x:x[1]))
        for key,val in count_sorted.items():
            ans.append(key)
            if len(ans)==k:
                break

        return ans
