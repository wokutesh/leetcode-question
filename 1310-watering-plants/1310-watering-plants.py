class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        a=-1
        step=0
        cap=capacity
        for i in range(len(plants)):
            if capacity>=plants[i]:
                step+=1
                capacity-=plants[i]

            else:
                step+=i-a+i-1-a
                capacity=cap
                capacity-=plants[i]

        return step

