class Game:

    game_ratings = 8.2
    def __init__(self, game_name, game_genre, game_year, game_price, game_size):
        self.game_name = game_name
        self.game_genre = game_genre
        self.game_year = game_year
        self.game_price = game_price
        self.game_size = game_size

game1 = Game("Red Dead Redemption 2", "Revenge,Action","2018","1084","118 GB")
game2 = Game("Resident Evil","Horror, Action","2019","889","78 GB")
game3 = Game("Spider Man","Adventure, Action","2021","1109","95 GB")

print(game1.game_name)
print(game1.game_size)
print(game1.game_genre)
print(game1.game_price)
print(game1.game_year)
print(Game.game_ratings)
