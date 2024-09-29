class Car:
    
    cars_number = 0
    
    def __init__(self , name , price):
        self.name = name
        self.price = price
        self.status = False
        Car.cars_number += 1
        
    def start(self):
        if self.status:
            print("car is already started :))")
        else:
            self.status = True
            print(f"your {self.name} started")
        
        
    def off(self):
        if self.status:
            print(f"your {self.name} is off")
        else:
            print(f'please first start your {self.name}')
        
        
car1 = Car("benz" , "250000")
car2 = Car("benz" , "250000")
car3 = Car("benz" , "250000")
car4 = Car("benz" , "250000")

# car1.start()
# print(car1.status)
# car1.off()

print(Car.cars_number)
