
from data_managers.load_json import read_json

def sort_movies():
    """Sort movies by rating or year."""
    print("========= Sort Movies =========")
    movies = read_json()

    valid_keys = {"rate", "year"}
    valid_orders = {"ascending": False, "descending": True}


    while True:
        sort_key = input("Which attribute do you want to sort by (rate or year)? ").lower()
        if sort_key in valid_keys:
            break
        print("Invalid input! Please enter 'rate' or 'year'.")


    while True:
        sort_order_input = input("In which order do you want to sort (ascending or descending)? ").lower()
        if sort_order_input in valid_orders:
            reverse_order = valid_orders[sort_order_input]
            break
        print("Invalid input! Please enter 'ascending' or 'descending'.")


    sorted_movies = dict(sorted(movies.items(), key=lambda item: item[1][sort_key], reverse=reverse_order))

    print("=================================")
    print(f"Sorted by {sort_key} in {sort_order_input} order:\n")
    for movie, infos in sorted_movies.items():
        print(f"{movie} ({infos['year']}): {infos['rate']}")

