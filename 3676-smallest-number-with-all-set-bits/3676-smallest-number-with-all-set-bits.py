class Solution:
    def smallestNumber(self, n: int) -> int:
        x=n
      

        while True:
            binary=bin(x)

            if set(binary[2:])=={'1'}:
                return x
                break
            x+=1