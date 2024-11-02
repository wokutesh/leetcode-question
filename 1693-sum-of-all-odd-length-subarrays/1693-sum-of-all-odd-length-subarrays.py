class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        count=0

        for i in range(len(arr)):
            
            for j in range(i + 1, len(arr) + 1):

                subarray = arr[i:j]
                if len(subarray)%2!=0:
                    count+=sum(subarray)
        return count
        

        