class Book():
    def __init__(self, Name, age) -> None:
        self.name=Name
        self.age=age
    def __str__(self) -> str:
        return("my name is Jaini")
#method overloading: in this 2 functions have the same name one in the parent class and one in the child class but their variables are different which makes them slightly different so overloading happens and both the functions are being called together
#method overriding: in this 2 functions have the same function name and variable name, one in parent and one in child, so the newer function in the child class replaces the one in the parent
