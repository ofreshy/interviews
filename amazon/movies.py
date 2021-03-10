class Movie(object):
    def __init__(self, id, rating, similar):
        self.id = id
        self.rating = rating
        self.similar = similar

    def __str__(self):
        return "<Movie id={0} rating={1}>".format(self.id, self.rating)


def getMovieRecommendations(movie, N):
    movies = explore_recurs(movie)
    if len(movies) <= N:
        return movies

    sorted_by_ratings = sorted(movies, key=lambda m: m.rating, reverse=True)
    return sorted_by_ratings[:N]


def explore_network(movie):
    """

    :param movie:
    :return: list with movies that are connected to this movie
    """
    movies_to_explore = [movie]
    explored_ids = set()
    explored_movies = list()

    while movies_to_explore:
        movie_to_explore = movies_to_explore.pop()
        mid = movie_to_explore.id
        if mid in explored_ids:
            continue
        explored_ids.add(movie_to_explore.id)
        explored_movies.append(movie_to_explore)
        movies_to_explore += movie_to_explore.similar

    # The first element is always our own movie
    return explored_movies[1:]


def explore_recurs(movie):
    visited = set()
    to_explore = [movie]
    explored = []

    def explore():
        if not to_explore:
            return
        m = to_explore.pop()
        if m.id not in visited:
            visited.add(m.id)
            explored.append(m)
            to_explore.extend(m.similar)
        # the recursive call
        explore()

    explore()
    return explored[1:]

assert getMovieRecommendations(Movie(1, 10, []), 1) == []

m1 = Movie(1, 1, [])
m2 = Movie(2, 2, [m1])
m3 = Movie(3, 3, [m1])
m4 = Movie(4, 10, [m2, m3])
m1.similar = [m2, m3]
m2.similar.append(m4)
m3.similar.append(m4)


assert getMovieRecommendations(m1, 1) == [m4]
assert getMovieRecommendations(m1, 2) == [m4, m3]
