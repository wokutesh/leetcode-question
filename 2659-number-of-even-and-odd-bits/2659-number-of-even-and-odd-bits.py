class Solution:
    def evenOddBit(self, n: int) -> List[int]:
        binary_n=bin(n)[2:]
        even=0
        odd=0
        for i,bit in enumerate(binary_n[::-1]):
            if bit=='1' :

                if i%2==0:
                    even+=1
           
                else:
                    
                    odd+=1

        return [even,odd]

