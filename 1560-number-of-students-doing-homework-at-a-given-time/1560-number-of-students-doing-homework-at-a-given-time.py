class Solution:
    def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:
        count=0
        for i ,j in zip(startTime,endTime):
            if queryTime>=i and queryTime<=j:
                count+=1
        return count
        