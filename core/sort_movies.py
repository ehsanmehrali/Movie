
from data_managers.load_json import read_json


def sort_movies():
    """ Sorting movies based on rating """
    print("========= Sorted Movies =========")

    movies = read_json()
    sorted_movies_descending = dict(sorted(movies.items(), key=lambda item: item[1]["rate"], reverse=True))

    print("By rating in Descending order: ")
    for movie, rate_obj in sorted_movies_descending.items():
        print(f"{movie}: {rate_obj['rate']}")