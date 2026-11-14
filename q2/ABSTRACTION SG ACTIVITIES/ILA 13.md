Look at this "Broken" code and say what’s wrong with it:


Python

class Animal(ABC):

    @abstractmethod

    def make_sound(self):

        pass

class Dog(Animal):

    def wag_tail(self):

        print("Wagging!")


# Teacher Question: If I run 'my_dog = Dog()', will it work?





ANSWER:

IT WONT WORK BECAUSE UR DOG CHILDCLASS DOESNT HAVE THE MAKE_SOUND METHOD WHICH IS REQUIRED BY THE AVBSTRACTT CLASSSS.