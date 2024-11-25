class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        max_index=0
        max_one=0
        for i,row in enumerate(mat):
            count_one=row.count(1)
            if count_one > max_one:
                max_one=count_one
                max_index=i

        return [max_index,max_one]
        



        