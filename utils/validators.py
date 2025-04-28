

def validate_rate(rate):
    return 0 < rate <= 10

def validate_year(year, current_year):
    first_movie_year = 1896
    return first_movie_year < year < current_year