import math
from datetime import datetime


from data_managers.load_json import read_json, write_json
from utils.text_utils import title_case_and_exceptions
from utils.validators import validate_rate, validate_year


def get_movie_name():
    name = input("Enter new movie name: ")
    if not name:
        raise ValueError("Empty movie name.")

    return title_case_and_exceptions(name)


def get_movie_rate():
    while True:
        try:
            rate = float(input("Enter movie rating (1-10): "))
            rate = math.trunc(rate * 10) / 10
            if validate_rate(rate):
                return rate

            print("Out of range (1-10)!")
        except ValueError:
            print("Invalid rating input!")
            return


def get_movie_year():
    current_year = datetime.now().year
    while True:
        try:
            year = int(input(f"Enter the year the movie was made (1896 till {current_year}): "))
            if validate_year(year, current_year):
                return year

            print(f"Invalid year (1896 till {current_year})!")
        except ValueError:
            print("Invalid year input!")
            return


def add_movie():
    """ Write """
    try:
        print("=========== Add movies ==========")
        new_movie_name = get_movie_name()
        movies = read_json()
        if new_movie_name in movies:
            print(f'Movie "{new_movie_name}" already exists!')
            return

        new_movie_rate = get_movie_rate()
        if new_movie_rate is None:
            return
        new_movie_year = get_movie_year()
        if new_movie_year is None:
            return

        movies[new_movie_name] = {"rate": new_movie_rate, "year": new_movie_year}
        write_json(movies)
        print(f'The movie "{new_movie_name} ({new_movie_year})" with a rating of {new_movie_rate} was successfully added.')

    except ValueError as e:
        print(e)
    except KeyboardInterrupt:
        print("\nBye!")
        exit()
