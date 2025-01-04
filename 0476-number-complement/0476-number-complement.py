class Solution:
    def findComplement(self, num: int) -> int:
        binary_num=bin(num)[2:]
        stack=[]
        for i in binary_num:
            if i=='0':
                stack.append('1')
            else:
                stack.append('0')
        str_stack=''.join(stack)
        return int(str_stack,2)