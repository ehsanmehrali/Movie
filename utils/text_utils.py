
def title_case_and_exceptions(text):
    exception_words = ["the", "a", "an", "and", "but", "or", "for", "nor", "in", "on", "at", "by", "of", "to", "up", "via"]
    return " ".join([word.capitalize() if word not in exception_words else word.lower() for word in text.split()])