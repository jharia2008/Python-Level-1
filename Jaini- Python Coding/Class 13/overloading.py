#method overloading: in this 2 functions have the same name one in the parent class and one in the child class but their variables are different which makes them slightly different so overloading happens and both the functions are being called together
class House:
    def __init__(self, bedroom, bathroom):
        self.bedroom= bedroom
        self.kitchen= 1
        self.bathroom= bathroom
    def floors(a):
        floor= str(input("Enter the number of floors"))
        print("The number of floors are " + floor + str(a))
class newHouse(House):
    def __init__(self, diningRoom):
        self.livingRoom= 1
        self.diningRoom= diningRoom
        self.officeRoom= 1
    def floors(x, y):
        floor=str(input("Enter the number of floors"))
        print("The number of floors are " + floor + str(x) + str(y))
HouseOwner1= newHouse(1)
print(HouseOwner1.floors("2"))
print(HouseOwner1.floors("3, 6"))