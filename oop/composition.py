class Engine:
    def __init__(self, horse_power):
        self.horse_power = horse_power

class Wheel:
    def __init__(self, size):
        self.size = size
        
    

class Car:
    def __init__(self, make, model, horse_power, wheel_size):
        self.make = make
        self.model = model
        self.engine = Engine(horse_power)
        self.wheels = [Wheel(wheel_size) for wheel in range(4)]
        
    def display_car_info(self):
         return f" Car make: {self.make} \n Car model: {self.make} \n Engine Horse Power: {self.engine.horse_power}(hp) \n Car Wheel size = {self.wheels[0].size}"
                
        
        
        
car1 = Car(make='Ford', model= 'Mustang', horse_power= 500, wheel_size= 18)

print(car1.display_car_info())
print()

car2 = Car(make="Chevrolet", model="Corvette", horse_power= 670, wheel_size= 19)
print(car2.display_car_info())

    
    