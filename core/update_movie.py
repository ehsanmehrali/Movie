import math

from data_managers.load_json import read_json, write_json
from core.add_movie import get_movie_name, get_movie_rate, get_movie_year


def update_movie():
    """ Update """
    print("========= Update movies =========")
    try:
        movie_to_update = get_movie_name(" ")
        movies = read_json()

        if movie_to_update not in movies:
            print(f"The movie '{movie_to_update}' does not exists!")
            return

        new_rate = get_movie_rate()
        if new_rate is None:
            return
        new_year = get_movie_year()
        if new_year is None:
            return

        movies[movie_to_update] = {"rate": new_rate, "year": new_year}
        write_json(movies)
        print(f"The movie '{movie_to_update} ({new_year})' with a new rating of {new_rate} has been updated.")

    except ValueError as e:
        print(e)
    except KeyboardInterrupt:
        print("\nBye!")
        exit()