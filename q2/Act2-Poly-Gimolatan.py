# 1. Answer the following questions:
# a. What is duck typing, as explained in the video?
#duck typing is like when you logically think about it, and it if it performs the same type of action just different categories, then you can use the same method. Regardless of how unrelated it is in topic.
# b. What did the Car class need to have so it could work inside the same loop as Dog and
# Cat, even if it does not inherit from the Animal class?
#it needed to have the same method name speak() as the other classes.


class Car:

    def move(self):
        print("The car drives on the road.")



class Boat:

    def move(self):
            print("The boat sails on water.")



class Drone:

    def move(self):
            print("The drone flies in the sky.")



def start_trip(vehicle):
     vehicle.move()


obj1 = Car()
obj2 = Boat()
obj3 = Drone()


start_trip(obj1)
start_trip(obj2)
start_trip(obj3)