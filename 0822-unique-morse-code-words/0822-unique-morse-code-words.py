class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        morse_code={'a':".-",'b':"-...",'c':"-.-.",'d':"-..",'e':".",'f':"..-.",'g':"--.",'h':"....",'i':"..",'j':".---",'k':"-.-",'l':".-..",'m':"--",'n':"-.",'o':"---",'p':".--.",'q':"--.-",'r':".-.",'s':"...",'t':"-",'u':"..-",'v':"...-",'w':".--",'x':"-..-",'y':"-.--",'z':"--.."}
        count=Counter()

        for word in words:
            trans=''
            for letter in word:
                trans+=morse_code[letter] 

            count[trans]+=1


        return len(count)
