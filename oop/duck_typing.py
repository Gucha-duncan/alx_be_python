#Duck typing is another way of achieving polymorphism besides inheritance

class Animal:
    alive = True
    
class Dog(Animal):
    def speak(self):
        print("Woof")
class Cat(Animal):
    
    def speak(self):
        print("Meow...")
        
class Car:
    alive = False
    def speak(self):
        print('Horn')
    

animals = [Dog(), Cat(), Car()]

for animal in animals:
    animal.speak()
    print(animal.alive)