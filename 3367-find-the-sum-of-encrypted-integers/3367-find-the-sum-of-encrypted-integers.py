class Solution:
    def sumOfEncryptedInt(self, nums: List[int]) -> int:

        def encrypt(x):
            
            res=[int(i) for i in str(x)]
            max_val=[]
            for j in range(len(res)):
                max_val.append(max(res))

            return int(''.join(map(str,max_val)))
        count=0
        for num in nums:
            count+=encrypt(num)

        return count




