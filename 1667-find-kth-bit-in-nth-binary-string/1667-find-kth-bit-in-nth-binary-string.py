class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        first = "0"
        second = "011"
        if k == 1:
            return "0"
        if k == 2:
            return "1"
        cur = second
        for i in range(3, n + 1):
        
            flipped = cur[::-1]
            inverted = ""
            for f in flipped:
                if f == "1":
                    inverted += "0"
                elif f == "0":
                    inverted += "1"
            cur = cur + "1" + inverted
           
    
       
        return cur[k - 1]
            