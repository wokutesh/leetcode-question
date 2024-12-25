class Solution:
    def splitNum(self, num: int) -> int:
        string=str(num)

        arr=[]
        for i in string:
            arr.append(i)

        sorted_str=sorted(string)

        arr1=''
        arr2=''

        for i in range(0,len(sorted_str),2):
            arr1+=sorted_str[i]

        for i in range(1,len(sorted_str),2):
            arr2+=sorted_str[i]

        return int(arr1)+ int(arr2)
        