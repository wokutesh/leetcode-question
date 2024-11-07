class Solution:
    def countTestedDevices(self, batteryPercentages: List[int]) -> int:
        count=0
        for i in range(len(batteryPercentages)):
            if batteryPercentages[i]>0:
                count+=1
                for j in range(i+1,len(batteryPercentages)):
                    batteryPercentages[j]=batteryPercentages[j]-1

        return count

                
        