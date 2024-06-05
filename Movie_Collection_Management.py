class MovieCollection:
    def __init__(self):
        self.movies = []

    def add_movie(self, title, director, year, genre):
        self.movies.append({'title': title, 'director': director, 'year': year, 'genre': genre})

    def update_movie(self, title, director, year, genre):
        for movie in self.movies:
            if movie['title'] == title:
                movie['director'] = director
                movie['year'] = year
                movie['genre'] = genre
                break

    def remove_movie(self, title):
        self.movies = [movie for movie in self.movies if movie['title'] != title]

    def view_collection(self):
        for movie in self.movies:
            print(f"Title: {movie['title']}, Director: {movie['director']}, Year: {movie['year']}, Genre: {movie['genre']}")

if __name__ == "__main__":
    my_collection = MovieCollection()
    my_collection.add_movie('Inception', 'Christopher Nolan', 2010, 'Science Fiction')
    my_collection.add_movie('The Godfather', 'Francis Ford Coppola', 1972, 'Crime')
    my_collection.update_movie('Inception', 'Christopher Nolan', 2010, 'Action')
    my_collection.remove_movie('The Godfather')
    my_collection.view_collection()
