
from fuzzywuzzy import process

from data_managers.load_json import read_json
from core.add_movie import get_movie_name


def show_search_res(matched_name, partial_matched_names, searched_name):
    movies = read_json()
    if matched_name :
        print("Exact match found!")
        print(f"{matched_name}, it's rated {movies[matched_name]['rate']}")
    elif partial_matched_names:
        print(f"The movie {searched_name} not found!")
        print("Do you mean: ")
        for i, movie in enumerate(partial_matched_names):
            print(f"{i + 1}- {movie}")
    else:
        print(f"No results found for '{searched_name}'")


def get_matched_movie(ratios, highest):
    matched_movie = ""
    partial_matched_movies = []

    for each_ratio in ratios:
        if 92 <= each_ratio[1] <= 100:
            matched_movie = highest[0]
        elif 80 <= each_ratio[1] < 92:
            partial_matched_movies.append(each_ratio[0])

    return matched_movie, partial_matched_movies


def search_movie():
    """ Search """
    print("============ Search =============")
    try:
        searched_movie = get_movie_name(" ")
        movies = read_json()
        movie_names = list(movies.keys())

        ratios = process.extract(searched_movie, movie_names)
        highest = process.extractOne(searched_movie, movie_names)

        matched_movie, partial_matched_movies = get_matched_movie(ratios, highest)
        show_search_res(matched_movie, partial_matched_movies, searched_movie)
    except ValueError as e:
        print(e)
