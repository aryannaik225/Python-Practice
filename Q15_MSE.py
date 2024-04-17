#Aryan Naik
# Wap to implement Multiple inheritance using two base classes
class Mother:
    def __init__(self):
        print("X chromosome from mother")
        self.dnaM = 'X'

class Father:
    def __init__(self) -> None:
        print("Y chromosome from father")
        self.dnaF = 'Y'

class Child(Mother, Father):
    def __init__(self):
        Mother.__init__(self)
        Father.__init__(self)
        self.display()

    def display(self):
        print("Child's chromosome is ",self.dnaM,self.dnaF)

obj = Child()