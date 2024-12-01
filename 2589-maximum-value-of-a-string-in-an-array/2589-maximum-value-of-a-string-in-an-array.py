class Solution:
    def maximumValue(self, strs: List[str]) -> int:
        max_length=0
        for char in strs:
            if char.isdigit():

                max_length=max(max_length,int(char))
            else:
                max_length=max(max_length,len(char))
        return max_length
        