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


def add_movie():
    """ Write """
    try:
        print("=========== Add movies ==========")
        new_movie_name = input("Enter new movie name: ")


        if new_movie_name:
            new_movie_name = title_case_and_exceptions(new_movie_name)
            movies = read_json()
            current_year = datetime.now().year
            if new_movie_name not in movies:
                movies[new_movie_name] = {}

                while True:
                    new_movie_rate = math.trunc(float(input(f"Enter {new_movie_name} rating (1-10): ")) * 10) / 10
                    if 1 <= new_movie_rate <= 10:
                        movies[new_movie_name]["rate"] = new_movie_rate

                        break
                    else:
                        print("Out of Range(1-10)!")

                while True:
                    new_movie_year = int(
                        input(f"Please enter the year the movie '{new_movie_name}' was made(1888-current year): "))
                    if 1888 <= new_movie_year <= current_year:
                        movies[new_movie_name]["year"] = new_movie_year
                        write_json(movies)
                        print(
                            f'The movie "{new_movie_name} ({new_movie_year})" with a rating of {new_movie_rate} was successfully added.')
                        break
                    else:
                        print("Invalid year(1888-current year)!")

            else:
                print(f'Movie "{new_movie_name}" already exists!')

        else:
            raise ValueError

    except ValueError:
        print("Invalid input!")
        print("Please Try again later.")
    except KeyboardInterrupt:
        print("\nBye!")
        exit()