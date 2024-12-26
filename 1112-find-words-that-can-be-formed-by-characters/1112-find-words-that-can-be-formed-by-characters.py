class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        count_char=Counter(chars)
        
        ans=0
       
        for word in words:
            count_word=Counter(word)
            is_valid=True
            for key,val in count_word.items():
                if val> count_char[key]:
                    is_valid=False
                    break

            if is_valid:
                ans+=len(word)

        return ans
                    
        
        