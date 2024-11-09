class Solution:
    def freqAlphabets(self, s: str) -> str:
     
        j_to_z={'1':'a','2':'b','3':'c','4':'d','5':'e','6':'f','7':'g','8':'h','9':'i','10#':'j','11#':'k','12#':'l','13#':'m','14#':'n','15#':'o','16#':'p','17#':'q','18#':'r','19#':'s','20#':'t','21#':'u','22#':'v','23#':'w','24#':'x','25#':'y','26#':'z'}
        res=''
        i=0
        while i<len(s):
            if  s[i:i+3] in j_to_z:
                res+=j_to_z[s[i:i+3]]
                i+=3
            elif s[i] in j_to_z:
                res+=j_to_z[s[i]]
                i+=1
            else:
                i+=1
                
        return res

        return res

