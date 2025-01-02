class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        vowels = set(['a', 'e', 'i', 'o', 'u'])
        r_l, res = [0], []

        for i in range(len(words)):
            if words[i][0] in vowels and words[i][-1] in vowels:
                r_l.append(r_l[-1] + 1)
            else:
                r_l.append(r_l[-1])
        
        for que in queries:
            l, r = que
            r += 1
            res.append(r_l[r] - r_l[l])
        
        return res

        