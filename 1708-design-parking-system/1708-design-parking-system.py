class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.big=big
        self.medium=medium
        self.small=small

        

    def addCar(self, carType: int) -> bool:
        if carType==1 and self.big>=1:
            self.big-=1
        elif carType==2 and self.medium>=1:
            self.medium-=1
        elif carType==3 and self.small>=1:
            self.small-=1
        else:
            return False
        return True 
        


# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)