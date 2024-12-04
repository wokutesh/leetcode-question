class Solution:
    def checkString(self, s: str) -> bool:
        a_list=[]
        b_list=[]
        if s.count('a')==0 :
            return True
        if s.count('b')==0:
            return True
        for idx,char in enumerate(s):
            if char=='a':
                a_list.append(idx)
            else:
                b_list.append(idx)

        if max(a_list)<min(b_list):
            return True
        else:
            return False