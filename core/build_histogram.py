
from matplotlib import pyplot as plt

from data_managers.load_json import read_json

def build_histogram():
    """ Histogram """
    movies = read_json()
    movies_rating_list = [item["rate"] for item in movies.values()]
    plt.hist(movies_rating_list, bins=10)
    plt.show()