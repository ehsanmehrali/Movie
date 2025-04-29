
from datetime import datetime

from data_managers.load_json import read_json

def filter_movies():
    print("========= Filter Movies =========")
    movies = read_json()
    first_movie_year = 1986
    current_year = datetime.now().year
    try:
        min_rate_input = input("Enter minimum rating (leave blank for no minimum rating): ")
        min_rate = float(min_rate_input) if min_rate_input else 1.0

        start_year_input = input("Enter start year (leave blank for no start year): ")
        start_year = int(start_year_input) if start_year_input else first_movie_year

        end_year_input = input("Enter end year (leave blank for no end year): ")
        end_year = int(end_year_input) if end_year_input else current_year
    except ValueError:
        print("Invalid input! Please enter valid numbers for rating and year.")
        return

    filtered = {
        title: info
        for title, info in movies.items()
        if info.get("rate", 0) >= min_rate and start_year <= info.get("year", 0) <= end_year
    }

    if filtered:
        print("\nFiltered movies:")
        for title, info in filtered.items():
            print(f"{title} ({info['year']}): {info['rate']}")
    else:
        print("No movies matched the criteria.")

