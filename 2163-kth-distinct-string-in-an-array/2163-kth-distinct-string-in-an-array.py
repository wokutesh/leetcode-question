class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        res=[]
        for ele in arr:
            if arr.count(ele)==1:
                res.append(ele)
        if len(res)<k:
            return ''

    

        return res[k-1]
        