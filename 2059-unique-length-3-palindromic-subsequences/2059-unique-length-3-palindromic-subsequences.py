class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        count = 0

        for char in ascii_lowercase:
            left_index = s.find(char)

            right_index = s.rfind(char)

            if right_index - left_index > 1:

                count += len(set(s[left_index + 1 : right_index]))

        return count