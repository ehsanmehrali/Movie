
from data_managers.load_json import read_json, write_json
from utils.text_utils import title_case_and_exceptions

def delete_movie():
    """ Delete """
    print("========= Delete movies =========")
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