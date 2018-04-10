#model.py
import csv

BB_FILE_NAME = 'umbball.csv'

bb_seasons = []

def init_bball(csv_file_name = BB_FILE_NAME):
    global bb_seasons
    with open(BB_FILE_NAME) as f:
        reader = csv.reader(f)
        next(reader)
        next(reader)
        global bb_seasons
        bb_seasons = []
        for r in reader:
            bb_seasons.append(r)


def get_bball_seasons(sortby='year', sortorder='desc'):
    if sortby == 'year':
        sortcol = 1
    elif sortby == 'wins':
        sortcol = 3
    elif sortby == 'pct':
        sortcol = 5
    else:
        sortcol = 0

    rev = (sortorder == 'desc')
    sorted_list = sorted(bb_seasons, key=lambda row: row[sortcol], reverse=rev)
    return sorted_list

init_bball(BB_FILE_NAME)
