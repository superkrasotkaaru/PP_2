movies = [
{
"name": "Usual Suspects", 
"imdb": 7.0,
"category": "Thriller"
},
{
"name": "Hitman",
"imdb": 6.3,
"category": "Action"
},
{
"name": "Dark Knight",
"imdb": 9.0,
"category": "Adventure"
},
{
"name": "The Help",
"imdb": 8.0,
"category": "Drama"
},
{
"name": "The Choice",
"imdb": 6.2,
"category": "Romance"
},
{
"name": "Colonia",
"imdb": 7.4,
"category": "Romance"
},
{
"name": "Love",
"imdb": 6.0,
"category": "Romance"
},
{
"name": "Bride Wars",
"imdb": 5.4,
"category": "Romance"
},
{
"name": "AlphaJet",
"imdb": 3.2,
"category": "War"
},
{
"name": "Ringing Crime",
"imdb": 4.0,
"category": "Crime"
},
{
"name": "Joking muck",
"imdb": 7.2,
"category": "Comedy"
},
{
"name": "What is the name",
"imdb": 9.2,
"category": "Suspense"
},
{
"name": "Detective",
"imdb": 7.0,
"category": "Suspense"
},
{
"name": "Exam",
"imdb": 4.2,
"category": "Thriller"
},
{
"name": "We Two",
"imdb": 7.2,
"category": "Romance"
}
]
def calculate_average_imdb_by_category(category_name, movies_list):
    """
    Function to calculate the average IMDb score of movies in a specific category.

    Parameters:
    - category_name (str): The category to filter movies.
    - movies_list (list): List of dictionaries representing movies.

    Returns:
    - float: Average IMDb score for movies in the specified category.
    """
    category_movies = [movie for movie in movies_list if movie["category"].lower() == category_name.lower()]

    if not category_movies:
        return 0.0

    total_score = sum(movie["imdb"] for movie in category_movies)
    average_score = total_score / len(category_movies)

    return average_score

# Example usage:
category_name = "Romance"
average_imdb_score = calculate_average_imdb_by_category(category_name, movies)
print(f"The average IMDb score of {category_name} movie is: {average_imdb_score:.2f}")