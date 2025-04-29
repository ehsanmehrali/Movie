# Built-in
import sys

# Local
from core.show_all_movies import show_all_movies
from core.add_movie import add_movie
from core.delete_movie import delete_movie
from core.update_movie import update_movie
from core.show_statistics import show_statistics
from core.random_movie import random_movie
from core.search_movie import search_movie
from core.sort_movies import sort_movies
from core.filter_movies import filter_movies
from core.build_histogram import build_histogram


def show_menu(items):
    """ Show menu items """
    divider = "================================="
    while True:
        print("============== Menu =============")
        for key, (desc, _) in items.items():
            print(f"{f"{key}.":{''}<3}", f"{desc}")


        try:
            print(divider)
            choice = int(input("Select from the menu (1-10): "))
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
        8: ("Sort movies by rating and release year", sort_movies),
        9: ("Filter movies by rate and release year", filter_movies),
        10: ("Create Rating Histogram", build_histogram)
    }
    show_menu(options)


def main():
    print(
        "******* My Movies Database *******")
    menu_items()


if __name__ == '__main__':
    main()