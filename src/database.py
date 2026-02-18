import csv

from config import SONGS_DB_PATH
from Song import Category, Song


def _read_data_from_csv():
    results = []

    with open(SONGS_DB_PATH, 'r') as songs_file:
        data = csv.reader(songs_file, delimiter=';')
        for row in data:
            results.append(row)

    return results[1:]  # skip heading row


def _get_categories_list(categories_str):
    categories = []

    for cat in categories_str.split(','):
        cat_upper = cat.upper()
        cat_format = cat_upper.replace("-", "_")
        try:
            categories.append(Category[cat_format])
        except:
            print(f"WARNING: Category {cat_format} is invalid")

    return categories


def get_songs():
    csv_data = _read_data_from_csv()
    songs = []

    for row in csv_data:
        categories = _get_categories_list(row[1])
        song = Song(row[0], categories, int(row[2]), int(row[3]))
        songs.append(song)

    return songs


def _filter_song_by_category(song, categories_filter):
    filter_check = True
    if categories_filter:
        for category in categories_filter:
            if category not in song.categories:
                filter_check = False

    return filter_check


def _filter_song_by_year(song, year_filter_start, year_filter_end):
    if year_filter_start and song.year < year_filter_start:
        return False

    if year_filter_end and song.year > year_filter_end:
        return False

    return True


def filter_songs(songs, categories, year_start, year_end):
    results = []

    for song in songs:
        filter_check = _filter_song_by_category(song, categories)
        if not filter_check:
            continue

        filter_check = _flter_songs_by_year(song, year_start, year_end)
        if filter_check:
            results.append(song)

    return results
