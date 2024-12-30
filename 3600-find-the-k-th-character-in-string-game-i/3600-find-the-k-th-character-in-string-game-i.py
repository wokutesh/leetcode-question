class Solution:
    def kthCharacter(self, k: int) -> str:
        count_char='abcdefghijklmnopqrstuvwxyz'

        word='a'
        while len(word)<k:
            temp=''
            for i in range(len(word)):
                if word[i]=='z':
                    temp+='a'

                idx=count_char.index(word[i])
                temp+=count_char[idx+1]

            word+=temp

        return word[k-1]
        