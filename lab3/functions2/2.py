movies = [
    {"name": "Usual Suspects", "imdb": 7.0, "category": "Thriller"},
    {"name": "Hitman", "imdb": 6.3, "category": "Action"},
    {"name": "Dark Knight", "imdb": 9.0, "category": "Adventure"},
    # ... (remaining movie entries)
]
def movies_above_5_5(movie_list):
    """
    Returns a sublist of movies with an IMDB score above 5.5.

    Parameters:
    - movie_list: List of movie dictionaries.

    Returns:
    - Sublist of movies with IMDB score above 5.5.
    """
    return [movie for movie in movie_list if movie["imdb"] > 5.5]

# Example usage:
result_sublist = movies_above_5_5(movies)
print(result_sublist)
