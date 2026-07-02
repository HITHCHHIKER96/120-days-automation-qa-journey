# multiple inheritance = inherit from more than one parent class
#                        C(A, B)

# multilevel inheritance = inherit from a parent who inherits from another parent
#                          C(B) <- B(A) <- A

class President:

    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f"{self.name} is eating")
    def sleep(self):
        print(f"{self.name} is sleeping")

class Prey(President):
    def flee(self):
        print(f"{self.name} is fleeing")
class Predator(President):
    def hunt(self):
        print(f"{self.name} is hunting")

class Deer(Prey):
    pass
class Lion(Predator):
    pass
class Fish(Prey, Predator):
    pass

deer = Deer("Rock")
lion = Lion("John")
fish = Fish("Puffy")

deer.flee()
deer.eat()
deer.sleep()

