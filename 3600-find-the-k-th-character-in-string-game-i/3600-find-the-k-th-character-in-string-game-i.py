class Solution:
    def kthCharacter(self, k: int) -> str:
        count_char = "abcdefghijklmnopqrstuvwxyz"
        word = "a"
        
        while len(word) < k:
            temp = ""
            for char in word:
                if char == "z":
                    temp += "a"
                else:
                    temp += count_char[count_char.index(char) + 1]
            word += temp
        
        return word[k - 1]
        