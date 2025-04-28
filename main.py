# Built-in
import sys
import random
import math
from datetime import datetime

# Third-party
from fuzzywuzzy import process
from matplotlib import pyplot as plt

# Local
from core.show_all_movies import show_all_movies
from core.add_movie import add_movie
from core.delete_movie import delete_movie
from core.update_movie import update_movie
from core.show_statistics import show_statistics
from data_managers.load_json import read_json, write_json




def title_case_and_exceptions(text):
    exception_words = ["the", "a", "an", "and", "but", "or", "for", "nor", "in", "on", "at", "by", "of", "to", "up", "via"]
    return " ".join([word.capitalize() if word not in exception_words else word.lower() for word in text.split()])


def random_movie():
    """ Recommended movie """
    print("======= Recommended movie =======")
    movies = read_json()
    movie, rating_obj = random.choice(list(movies.items()))
    print(f"Your movie for tonight: \n{movie}, it's rated {rating_obj["rate"]}")


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


def search_movie():
    """ Search """
    print("============ Search =============")
    searched_movie = input("Enter a part of movie name: ")

    if searched_movie:
        movies = read_json()
        searched_movie = title_case_and_exceptions(searched_movie)
        movie_names = list(movies.keys())

        ratios = process.extract(searched_movie, movie_names)
        highest = process.extractOne(searched_movie, movie_names)

        matched_movie = ""
        partial_matched_movies = []

        for each_ratio in ratios:
            if 92 <= each_ratio[1] <= 100:
                matched_movie = highest[0]
            elif 80 <= each_ratio[1] < 92:
                partial_matched_movies.append(each_ratio[0])

        show_search_res(matched_movie, partial_matched_movies, searched_movie)


def sort_movies():
    """ Sorting movies based on rating """
    print("========= Sorted Movies =========")
    movies = read_json()
    sorted_movies_descending = dict(sorted(movies.items(), key=lambda item: item[1]["rate"], reverse=True))
    print("By rating in Descending order: ")
    for movie, rate_obj in sorted_movies_descending.items():
        print(f"{movie}: {rate_obj['rate']}")


def build_histogram():
    """ Histogram """
    movies = read_json()
    movies_rating_list = [item["rate"] for item in movies.values()]
    plt.hist(movies_rating_list, bins=10)
    plt.show()


def show_menu(items):
    """ Show menu items """
    divider = "================================="
    while True:
        print("============== Menu =============")
        for key, (desc, _) in items.items():
            print(f"{key}. {desc}")

        try:
            print(divider)
            choice = int(input("Select from the menu (1-9): "))
            print(divider)

            if choice in items:
                items[choice][1]()
                print(divider)
                input("Press enter to continue: ")
            else:
                print("Invalid option!\n")

        except ValueError:
            print("Invalid input!\n")
        except KeyboardInterrupt:
            items[0][1]()


def menu_items():
    """ Dispatcher dict for menu items """
    # Exit function
    bye = lambda: (print("\nBye!") or sys.exit())

    # Dispatcher dict
    options = {
        0: ("Exit", bye),
        1: ("List movies", show_all_movies),
        2: ("Add movie", add_movie),
        3: ("Delete movie", delete_movie),
        4: ("Update movie", update_movie),
        5: ("Stats", show_statistics),
        6: ("Random movie", random_movie),
        7: ("Search movie", search_movie),
        8: ("Movies sorted by rating", sort_movies),
        9: ("Create Rating Histogram", build_histogram)
    }
    show_menu(options)


def main():
    print(
        "******* My Movies Database *******")
    menu_items()


if __name__ == '__main__':
    main()

# structure of data in json file was edited!!