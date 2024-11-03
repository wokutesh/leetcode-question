class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        res=[]
        for element in image:
            ele_sorted=element[::-1]
            for i in range(len(ele_sorted)):
                if ele_sorted[i]==1:
                    ele_sorted[i]=0

                elif ele_sorted[i]==0:
                    ele_sorted[i]=1

            res.append(ele_sorted)

        return res
        