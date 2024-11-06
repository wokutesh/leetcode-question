class Solution:
    def minimumPushes(self, word: str) -> int:
        counter = Counter(word)
        res = 0
        sorted_items= sorted(counter.items(), key=lambda x: x[1], reverse=True)
        for i, e in enumerate(sorted_items):
            res += (i//8+1) * e[1]
        return res         