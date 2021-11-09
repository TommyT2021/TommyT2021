class ParkingLot:
    def __init__(self, name, totalSpaces, filledSpaces):
        self.name = name
        self.totalSpaces = totalSpaces
        self.filledSpaces = filledSpaces
    def __str__(self):
        return "Lot: " + str(self.name) + "\nFilled spaces: " + str(self.filledSpaces) + "\nTotal spaces: " + str(self.totalSpaces) + "\n"
    def letCarIn(self):
        if self.filledSpaces != self.totalSpaces:
            self.filledSpaces += 1
            return "Open Gate"
        else:
            return "Lot full, gate stays closed"
    def letCarOut(self):
        self.filledSpaces -= 1
        return "Open Gate"
    def lotStatus(self):
        if self.filledSpaces != self.totalSpaces:
            return "Spaces available"
        else:
            return "No spaces available"
    def getFilledSpaces(self):
        return self.filledSpaces

lot1 = ParkingLot("Downtown", 80, 79)
lot2 = ParkingLot("Northside", 40, 20)
print(lot1)
print(lot1.lotStatus())
gateAction = lot1.letCarIn()
print(gateAction)
print(lot1.lotStatus())
gateAction = lot1.letCarIn()
print(gateAction)
gateAction = lot1.letCarOut()
print(gateAction)
print(lot1)
print(lot2)
