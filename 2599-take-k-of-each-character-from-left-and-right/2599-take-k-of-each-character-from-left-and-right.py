class Solution:
    def takeCharacters(self, s: str, k: int) -> int:
        if k == 0:
            return 0

        
        freq = Counter(s)
        
        
        if freq['a'] < k or freq['b'] < k or freq['c'] < k:
            return -1

    
        n = len(s)
        left = 0

        for right in range(n):
            freq[s[right]] -= 1

    
            if freq['a'] < k or freq['b'] < k or freq['c'] < k:
                freq[s[left]] += 1
                left += 1

        return n -  (right - left + 1)
       