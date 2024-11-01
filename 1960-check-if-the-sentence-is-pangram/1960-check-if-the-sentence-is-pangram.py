class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        s='abcdefghijklmnopqrstuvwxz'
        return set(string.ascii_lowercase).issubset(sentence)

        