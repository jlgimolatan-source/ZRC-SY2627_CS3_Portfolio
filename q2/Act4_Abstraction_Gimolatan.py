from abc import ABC, abstractmethod


class Sensor(ABC):

    def __init__(self, substance, reading:int):
        self.substance = substance
        self.reading = reading
    
    @abstractmethod
    def get_reading(self, substance, reading):
        pass


class PHSensor(Sensor):

    def __init__(self, substance, reading):
        super().__init__(substance, reading)
        
    def get_reading(self):
        return(f"[pH Sensor] Reading: Your {self.substance} is {self.reading} PH")



class TempSensor(Sensor):

    def __init__(self, substance, reading):
        super().__init__(substance, reading)

    def get_reading(self):
        return(f"[Temperature Sensor] Reading: Your {self.substance} is {self.reading}°C")

    

subs1 = PHSensor("Beach Water", 7.2)
subs2 = TempSensor("Coffee", 24.5)


print("--- Lab Inventory System ---")
print(subs1.get_reading())
print(subs2.get_reading())
print()
print("------------------------------")