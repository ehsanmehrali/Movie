# Built-in
import sys

# Third-party

# Local
from data_managers.load_json import read_json, write_json


def show_all_movies():
    """ Read """
    print("********** Show movies **********")
    movies = read_json()

    print(f"There is {len(movies)} movies in total: ")
    for i, (name, rate) in enumerate(movies.items(),1):
        print(f"{i}- {name} : {rate}")


def title_case_and_exceptions(text):
    exception_words = ["the", "a", "an", "and", "but", "or", "for", "nor", "in", "on", "at", "by", "of", "to", "up", "via"]
    return " ".join([word.capitalize() if word not in exception_words else word.lower() for word in text.split()])


def add_movie():
    """ Write """
    try:
        print("********** Add movies **********")
        new_movie_name = input("Enter new movie name: ")

        if new_movie_name:
            new_movie_name = title_case_and_exceptions(new_movie_name)
            movies = read_json()

            if new_movie_name not in movies:

                while True:
                    new_movie_rate = float(input(f"Enter {new_movie_name} rating (1-10): "))
                    if 1 <= new_movie_rate <= 10:
                        movies[new_movie_name] = new_movie_rate
                        write_json(movies)
                        print(f'The movie "{new_movie_name}" with a rating of {new_movie_rate} was successfully added.')
                        break
                    else:
                        print("Out of Range(1-10)!")

            else:
                print(f'Movie "{new_movie_name}" already exists!')

        else:
            raise ValueError

    except ValueError:
        print("Invalid input!")
        print("Please Try again")
    except KeyboardInterrupt:
        print("\nBye!")
        exit()


def delete_movie():
    """ Delete """
    print("********** Delete movies **********")
    movie_to_delete = input("Enter movie name to delete: ")

    if movie_to_delete:
        movies = read_json()
        movie_to_delete = title_case_and_exceptions(movie_to_delete)

        if movie_to_delete in movies:
            movies.pop(movie_to_delete)
            write_json(movies)
            print(f"The movie '{movie_to_delete}' was successfully removed.")# The film "Lie" was successfully removed.
        else:
            print(f'The movie "{movie_to_delete}" does not exists!')

def update_movie():
    """ Update """
    print("********** Update movies **********")
    try:
        movie_to_update = input("Enter movie name: ")

        if movie_to_update:
            movies = read_json()
            movie_to_update = title_case_and_exceptions(movie_to_update)

            if movie_to_update in movies:
                new_rate = float(input("Enter new rating (0-10): "))

                if 0 < new_rate <= 10:
                    movies[movie_to_update] = new_rate
                    write_json(movies)
                    print(f"The movie '{movie_to_update}' with a new rating of {new_rate} has been updated.")
                else:
                    print("Out of Range(1-10)!")

            else:
                print(f"The movie '{movie_to_update}' does not exists!")

    except ValueError:
        print("Invalid input!")
        print("Please Try again")
    except KeyboardInterrupt:
        print("\nBye!")
        exit()

def show_statistics():
    """ Statistics """
    print("********** State **********")
    movies = read_json()
    ratings = list(movies.values())
    sorted_ratings = sorted(ratings)

    # Avr rating
    average_rate = sum(ratings) / len(ratings)

    # Median rating
    middle = len(ratings) // 2
    if len(sorted_ratings) % 2 != 0:
        median_rating = sorted_ratings[middle]
    else:
        median_rating = (sorted_ratings[middle - 1] + sorted_ratings[middle]) / 2
    # Best and worst movies
    best_movie = max(movies, key=movies.get)
    worst_movie = min(movies, key=movies.get)

    print(f"Average rating: {average_rate:.1f}")
    print(f"Median rating: {median_rating:.1f}")
    print(f"Best movie: {best_movie}, {movies[best_movie]}")
    print(f"Worst movie: {worst_movie}, {movies[worst_movie]}")



def random_movie():
    """ Recommended movie """
    pass

def search_movie():
    """ Search """
    pass


def sort_movies():
    """ Sorting movies based on rating """
    pass


def build_histogram():
    """ Histogram """
    pass

def show_menu(items):
    """ Show menu items """
    while True:
        print("Menu: ")
        for key, (desc, _) in items.items():
            print(f"{key}. {desc}")

        try:
            choice = int(input("\nSelect from the menu (1-9): "))
            print()

            if choice in items:
                items[choice][1]()
                input("\nPress enter to continue: ")
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
        "********************** My Movies Database **********************\n")
    menu_items()

if __name__ == '__main__':
    main()
