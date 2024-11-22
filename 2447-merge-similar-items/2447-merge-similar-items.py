class Solution:
    def mergeSimilarItems(self, items1: List[List[int]], items2: List[List[int]]) -> List[List[int]]:
        dict_={}
        for key,val in items1:
            dict_[key]=dict_.get(key,0)+val

        for key,val in items2:
            dict_[key]=dict_.get(key,0)+val

        res=[[key,val] for key,val in sorted(dict_.items())]
        return res