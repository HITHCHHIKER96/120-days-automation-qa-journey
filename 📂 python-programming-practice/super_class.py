# Super = Functions used in a child class to call methods from a parent class (superclass).
#         Allows you to extend the functionality of the inherited methods

class Korea:
    def __init__(self, beauty, food, dream_home):
        self.beauty = beauty
        self.food = food
        self.dream_home = dream_home

class Weather(Korea):
    def __init__(self, beauty, food, dream_home, weather_korea):
        super().__init__(beauty, food, dream_home)
        self.weather_korea = weather_korea

    def describe(self):
        print(f"The weather of Korea is {self.weather_korea} too beautiful")

class Places(Korea):
    def __init__(self, beauty, food, dream_home, peace):
        super().__init__(beauty, food, dream_home)
        self.peace = peace

class Price(Korea):
    def __init__(self, beauty, food, dream_home, price):
        super().__init__(beauty, food, dream_home)
        self.price = price

weather = Weather("Too Good","Too Delicious","Mine","Too Damn")
places = Places("Too Good","Too Delicious","Mine","Too Satisfactory")
price = Price("Too Good","Delicious","Mine","High")


print(places.dream_home)
print(places.food)
print(places.beauty)
print(places.peace)

weather.describe()