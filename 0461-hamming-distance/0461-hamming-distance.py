class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        x_binary=bin(x)[2:]
        y_binary=bin(y)[2:]

        max_length=max(len(x_binary),len(y_binary))
        x_binary=x_binary.zfill(max_length)
        y_binary=y_binary.zfill(max_length)
        count=0
        x_list=list(x_binary)
        y_list=list(y_binary)

       
      
        for i,j in zip(x_list,y_list):
            if i!=j:
                count+=1

        return count
        