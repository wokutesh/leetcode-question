class Solution:
    def minTimeToType(self, word: str) -> int:
        s='abcdefghijklmnopqrstuvwxyz'
        start_letter=0
        sum_=0
        for char in word:
            target=s.index(char)
            clockwise=abs(target-start_letter)
            anticlockwise= 26-clockwise
            sum_+=min(clockwise,anticlockwise)
            start_letter=target
        return sum_ + len(word)


