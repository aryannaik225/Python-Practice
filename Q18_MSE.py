#Aryan Naik
class Animal:
    def make_sound(self):
        print("Generic animal sound")

class Dog(Animal):
    def make_sound(self):
        print("Woof woof")

class Cat(Animal):
    def make_sound(self):
        print("Meow")

dog = Dog()
cat = Cat()

dog.make_sound()  
cat.make_sound()  
