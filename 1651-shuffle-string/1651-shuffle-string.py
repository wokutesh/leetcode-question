class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:

        res=[(string,index) for string ,index in zip(s,indices)]
        res.sort(key=lambda x:x[1])

        str_1=''
        for i in res:
            str_1+=i[0]
        return str_1

        