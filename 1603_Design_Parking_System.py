class ParkingSystem:
    def __init__(self, big: int, medium: int, small: int):
        self.slots = {1 : big, 2 : medium, 3 : small}
        self.occupied = dict.fromkeys(range(1,4), 0)
    def addCar(self, carType: int) -> bool:
        if self.occupied[carType] < self.slots[carType]:
            self.occupied[carType] += 1
            return True
        return False
