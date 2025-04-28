# Built-in
import sys

# Third-party

from matplotlib import pyplot as plt

# Local
from core.show_all_movies import show_all_movies
from core.add_movie import add_movie
from core.delete_movie import delete_movie
from core.update_movie import update_movie
from core.show_statistics import show_statistics
from core.random_movie import random_movie
from core.search_movie import search_movie
from data_managers.load_json import read_json


def title_case_and_exceptions(text):
    exception_words = ["the", "a", "an", "and", "but", "or", "for", "nor", "in", "on", "at", "by", "of", "to", "up", "via"]
    return " ".join([word.capitalize() if word not in exception_words else word.lower() for word in text.split()])


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