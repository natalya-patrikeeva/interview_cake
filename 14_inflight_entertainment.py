# Write a function that takes an integer flight_length (in minutes) and a list
# of integers movie_lengths (in minutes) and returns a boolean indicating
# whether there are two numbers in movie_lengths whose sum equals flight_length.

def two_movies_sum(flight_length, movie_lengths) :

    movies_seen = set()

    for movie in movie_lengths :
        # Save movies to a set for fast lookups
        second_movie = flight_length - movie

        if second_movie in movies_seen :
            return True

        movies_seen.add(movie)
        print movies_seen

    return False



print(two_movies_sum(50, [3, 30, 10, 4, 20]))
