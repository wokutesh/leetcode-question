class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        for _ in range(k):
            max_val=max(gifts)
            idx=gifts.index(max_val)
            
            gifts[idx]=math.floor(math.sqrt(max_val))

        return sum(gifts)