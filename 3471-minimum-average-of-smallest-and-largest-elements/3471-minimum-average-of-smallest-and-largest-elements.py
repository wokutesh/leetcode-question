class Solution:
    def minimumAverage(self, nums: List[int]) -> float:
        average=[]
        for i in range(len(nums)//2):
            max_n=max(nums)
            min_n=min(nums)

            average.append((min_n + max_n)/2)
            nums.remove(min_n)
            nums.remove(max_n)
        
        return min(average)

        