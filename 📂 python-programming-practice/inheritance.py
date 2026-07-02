# Inheritance = Allows a class to inherit attributes and methods form another class
#               Helps with code reusability and extensibility
#               class child(Parent)

class Animal:

    def __init__(self,name):
        self.name = name
        self.is_alive = False

    def eat(self):
        print(f"{self.name} is eating")

    def sleep(self):
        print(f"{self.name} is sleeping")

class Dog(Animal):
    pass

class Cat(Animal):
    pass

class Tiger(Animal):
    pass

dog = Dog("Modi")
cat = Cat("Nirmala")
tiger = Tiger("Royal Bengal")


print(dog.name)
print(dog.is_alive)
dog.eat()
dog.sleep()

