class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:
        l, r, res, n = 0, 0, 0, len(nums)
        freq = defaultdict(int)
        while r < n :
            freq[nums[r]] += 1
            while max(freq) - min(freq) > 2:
                freq[nums[l]] -= 1
                if freq[nums[l]] == 0:
                    del freq[nums[l]]
                l += 1
            res += r-l+1
            r+= 1
        return res