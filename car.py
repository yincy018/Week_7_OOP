class Car:
    def __init__(self, topSpeed, speed = 0):
        self.setTopSpeed(topSpeed)
        self.__speed = speed
    
    def setTopSpeed(self,topSpeed):
        if topSpeed > 0:
            self.__top_speed = topSpeed
        else:
            raise Exception(f"Invalid top speed: { topSpeed}")
    
    def getTopSpeed(self):
        return self.__top_speed

    def getSpeed(self):
        return self.__speed
    
    def accelerate(self):
        if self.__speed < self.__top_speed:
            self.__speed += 10
        else: 
            raise Exception (f"Cannot accelerate above top speed: {self.__top_speed}")
        
    def decelerate(self):
        if self.__speed < 0:
            raise Exception("Cannot decelerate below zero") 
        else:
            self.__speed -= 10   
            
      
    def __str__(self):
        return f"Car going {self.__speed}/{self.__top_speed} kmph"