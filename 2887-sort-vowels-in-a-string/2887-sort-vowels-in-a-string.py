class Solution:
    def sortVowels(self, s: str) -> str:
        vowels=set('aeiouAEIOU')
        arr=[x for x in s if x in vowels]
        arr.sort(reverse=True)
        res=''
        for char in s:
            if char in vowels:
                c=arr.pop()
                res+=c
            else:
                res+=char

        return res


        