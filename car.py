class SpeedException(Exception):
    pass


class Car:
    def __init__(self, topSpeed, speed = 0):
        self.setTopSpeed(topSpeed)
        self.__speed = speed
        self.__driver = None

    def set_driver(self, driver):
        self.__driver = driver

    def get_driver(self):
        return self.__driver

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
        if self.__driver is None:
            raise NoDriverException()
        
        if self.__speed < self.__top_speed:
            self.__speed += 10
        else: 
            raise SpeedException(f"Cannot accelerate above top speed: {self.__top_speed}")
        
    def decelerate(self):
        if self.__driver is None:
            raise NoDriverException()
        
        if self.__speed > 0:
            self.__speed -= 10   
            
        else:
            raise SpeedException("Cannot decelerate below zero") 
            
            
      
    def __str__(self):
        if self.__driver is None:
            raise NoDriverException
        else:
            return f"Car going {self.__speed}/{self.__top_speed} kmph"

class NoDriverException(Exception):
    def __init__(self):
        super().__init__("Cannot drive without a Driver")


  
car1 = Car(250, )
car1.set_driver(None)
car1.get_driver()
# print
try:
    for i in range(1,31):
        car1.accelerate()
        print(f'{car1}')
    
    print(f'Car driver by {car1.get_driver}\n{car1}')
except Exception as e:
    print(e)

    for i in range(1,31):
        try:
            car1.getSpeed()
            car1.decelerate()
            print(f'{car1}')
        except Exception as e:    
            print(e)

try:
    user = float(input("Please enter a number for a car top speed: "))
    car1.setTopSpeed(user)
    car1.getTopSpeed()
    print(f'{car1}')
except Exception as e:
    print(e)

try:
    car2 = Car(-99, )
    print(car2)
except Exception as e:
    print(e)