from Game import Game

def initialize_app():
    players = ["Player 1", "Player 2"]
    filters = None

    game = Game(players, filters)
    game.start()

if __name__ == "__main__":
    initialize_app()
