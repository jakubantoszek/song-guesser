import os
from enum import Enum

from config import SONGS_DIR_PATH

class Category(Enum):
    ROCK = 0,
    POP = 1,
    POP_ROCK = 2,
    METAL = 3,
    RAP = 4,
    POLISH = 10,
    NON_POLISH = 11


class Song:
    def __init__(self, file_name, categories, level, year):
        self.artist = file_name.split(" - ")[0]
        self.title = file_name.split(" - ")[1].split('.')[0]
        self.path = os.path.join(SONGS_DIR_PATH, file_name)
        self.categories = categories
        self.year = year
        self.level = level
