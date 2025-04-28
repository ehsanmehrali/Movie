
from data_managers.load_json import read_json

def show_all_movies():
    """ Read """
    print("========== Show movies ==========")
    movies = read_json()

    print(f"There is {len(movies)} movies in total: ")
    for i, (name, movie_info) in enumerate(movies.items(),1):
        print(f"{i}- {name} ({movie_info["year"]}): {movie_info["rate"]}")
