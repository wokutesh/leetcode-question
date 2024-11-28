class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key=lambda item: item[1], reverse=True)
        count=0
        size_sum=0
        for i,interval in enumerate(boxTypes):
            size,load=interval
            size_sum+=size
            if size_sum>truckSize:
                size_sum_diff=size_sum-truckSize
                count+=(size-size_sum_diff)*load
                break
            else:

                count+= size * load

        return count
            
        