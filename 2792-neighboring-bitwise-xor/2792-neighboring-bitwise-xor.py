class Solution:
    def doesValidArrayExist(self, derived: List[int]) -> bool:
        xor_sum=0
        for i in derived:
            xor_sum^=i
        if xor_sum==0:
            return True
        else:
            return False