class Solution:
    def stringHash(self, s: str, k: int) -> str:
        hash_value = {
        'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7, 'i': 8, 'j': 9,
        'k': 10, 'l': 11, 'm': 12, 'n': 13, 'o': 14, 'p': 15, 'q': 16, 'r': 17, 's': 18,
        't': 19, 'u': 20, 'v': 21, 'w': 22, 'x': 23, 'y': 24, 'z': 25
    }

        result = []
        n = len(s)
        
        for i in range(0, n ,k): 
            val_letter = 0
            substring = s[i:i + k]  

            for char in substring:  
                val_letter += hash_value[char]

            remainder = val_letter % 26 
            key = next((k for k, v in hash_value.items() if v == remainder), None)  
            if key:
                result.append(key)
        return ''.join(result) 

