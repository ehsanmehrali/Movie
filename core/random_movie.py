
import random

from data_managers.load_json import read_json

def random_movie():
    """ Recommended movie """
    print("======= Recommended movie =======")
    movies = read_json()
    movie, infos = random.choice(list(movies.items()))
    print(f"Your movie for tonight: \n{movie} ({infos["year"]}), it's rated {infos["rate"]}")