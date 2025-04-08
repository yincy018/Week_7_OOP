class SpeedException(Exception):
    pass


class Car:
    def __init__(self, topSpeed, speed = 0):
        self.setTopSpeed(topSpeed)
        self.__speed = speed
    
    def setTopSpeed(self,topSpeed):
        if topSpeed > 0:
            self.__top_speed = topSpeed
        else:
            raise SpeedException(f"Invalid top speed: { topSpeed}")
    
    def getTopSpeed(self):
        return self.__top_speed

    def getSpeed(self):
        return self.__speed
    
    def accelerate(self):
        if self.__speed < self.__top_speed:
            self.__speed += 10
        else: 
            raise SpeedException(f"Cannot accelerate above top speed: {self.__top_speed}")
        
    def decelerate(self):
        if self.__speed < 0:
            raise SpeedException("Cannot decelerate below zero") 
        else:
            self.__speed -= 10   
            
      
    def __str__(self):
        return f"Car going {self.__speed}/{self.__top_speed} kmph"
    
car1 = Car(250, )
try:
    for i in range(1,31):
        car1.accelerate()
        print(car1)
    car1.getSpeed()
    print(car1)
except Exception as e:
    print(e)

    for i in range(1,31):
        try:
            car1.getSpeed()
            car1.decelerate()
            print(car1)
        except Exception as e:    
            print(e)

try:
    user = float(input("Please enter a number for a car top speed: "))
    car1.setTopSpeed(user)
    car1.getTopSpeed()
    print(car1)
except Exception as e:
    print(e)

try:
    car2 = Car(-99, )
    print(car2)
except Exception as e:
    print(e)