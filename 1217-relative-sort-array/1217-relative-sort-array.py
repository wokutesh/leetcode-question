class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        
        map_idx={val:idx for idx,val in enumerate(arr2)}
        arr1.sort(key=lambda x: (map_idx.get(x, len(arr2)), x))
    
        return arr1

