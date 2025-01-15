class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        mask = 0
        result = 0
        for i in range(31, -1, -1):
            mask |= (1 << i)
            seen = set()
            for num in nums:
                seen.add(num & mask)
            candidate = result | (1 << i)
            for prefix in seen:
                if prefix ^ candidate in seen:
                    result = candidate
                    break
        return result