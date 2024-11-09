class Solution:
    def luckyNumbers(self, matrix: List[List[int]]) -> List[int]:
        res=[]
        for i in range(len(matrix)):

            mn_vl=min(matrix[i])
            col_index=matrix[i].index(mn_vl)
            is_luck=True
            for j in range(len(matrix)):
                if matrix[j][col_index]>mn_vl:
                    is_luck=False

                    break
            if is_luck:
                res.append(mn_vl)
        return res
        