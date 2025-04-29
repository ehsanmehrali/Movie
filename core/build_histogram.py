import os
import matplotlib

matplotlib.use('Agg')

import matplotlib.pyplot as plt
import numpy as np

from data_managers.load_json import read_json

ROOT_DIRECTORY = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
FILE_PATH = os.path.join(ROOT_DIRECTORY, "core", "build_histogram.py")

def build_histogram():
    """ Histogram """
    movies = read_json()
    movies_rating_list = [infos["rate"] for movie, infos in movies.items()]

    plt.figure(figsize=(10, 6))
    plt.hist(movies_rating_list, bins=20, edgecolor='black', alpha=0.75, color='royalblue')

    mean_rating = float(np.mean(movies_rating_list))
    plt.axvline(mean_rating, color='red', linestyle='dashed', linewidth=2,
                label=f'Average Rating: {mean_rating:.2f} IMDb')

    plt.title('Distribution of Ratings', fontsize=14)
    plt.xlabel('Rating (IMDb)', fontsize=12)
    plt.ylabel('Frequency', fontsize=12)
    plt.legend()

    plt.savefig("rating_histogram.png")

    # The user can click on the link and view the histogram image in the browser(just in my workspace in codio server).
    print("✅ Histogram saved. Open this address to view in browser:")
    print("🔗 https://prosperbagel-cairoradical.codio.io/Movie/rating_histogram.png")

    # plt.hist(movies_rating_list, bins=10)
    # plt.show()