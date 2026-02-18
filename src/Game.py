from dataclasses import dataclass

from config import NO_OF_SONGS_IN_GAME

@dataclass
class Player:
    name: str
    points: int = 0

class Game:
    def __init__(self, players, filter):
        self.players = []
        for p in players:
            self.players.append(Player(p, 0))

        self.songs = self._get_list_of_songs(NO_OF_SONGS_IN_GAME, filter)

    def _get_list_of_songs(self, number, filter):
        


    def start():
        pass
