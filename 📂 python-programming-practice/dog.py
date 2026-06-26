class Dog:
    def __init__(self, name, age, color):
        self.name = name
        self.age = age
        self.color = color

    def feed(self):
        print(f"You feed {self.name}")

    def walikng(self):
        print(f"You take a walk with {self.name}")