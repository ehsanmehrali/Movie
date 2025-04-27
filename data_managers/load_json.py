
import json
import os

ROOT_DIRECTORY = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
FILE_PATH = os.path.join(ROOT_DIRECTORY, "data", "movies.json")

def read_json():
    with open(FILE_PATH, "r", encoding="UTF-8") as handle:
        return json.load(handle)

def write_json(movies_data):
    with open(FILE_PATH, "w", encoding="UTF-8") as handle:
        json.dump(movies_data, handle)
