
from data_managers.load_json import read_json


def calc_avr_rating(ratings):
    return sum(ratings) / len(ratings)


def calc_median_rating(ratings, sorted_ratings):
    middle = len(ratings) // 2
    if len(sorted_ratings) % 2 != 0:
        return sorted_ratings[middle]
    else:
        return (sorted_ratings[middle - 1] + sorted_ratings[middle]) / 2


def best_and_worst(state, movies):
    return state(movies.items(), key=lambda item: item[1]['rate'])


def show_statistics():
    """ Statistics """
    print("============= State =============")
    movies = read_json()

    ratings =[item["rate"] for item in list(movies.values())]
    sorted_ratings = sorted(ratings)

    # Avr rating
    average_rate = calc_avr_rating(ratings)

    # Median rating
    median_rating = calc_median_rating(ratings, sorted_ratings)

    # Best and worst movies
    best_movie, max_rate_obj = best_and_worst(max, movies)
    worst_movie, min_rate_obj = best_and_worst(min, movies)

    print(f"Average rating: {average_rate:.1f}")
    print(f"Median rating: {median_rating:.1f}")
    print(f"Best movie: {best_movie} ({movies[best_movie]["year"]}), {max_rate_obj["rate"]}")
    print(f"Worst movie: {worst_movie} ({movies[best_movie]["year"]}), {min_rate_obj["rate"]}")