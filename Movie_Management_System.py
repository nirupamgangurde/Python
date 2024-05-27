class Movie:
    def __init__(self, title, director, year, rating):
        self.title = title
        self.director = director
        self.year = year
        self.rating = rating

    def __str__(self):
        return f"title:{self.title},director:{self.director},year:{self.year},rating:{self.rating}"

class Movie_database:
    def __init__(self):
        self.movies = []

    def add_movie(self, movie):
        self.movies.append(movie)


    def view_movie(self):
        return self.movies

    def search_movie(self, title):
        for movie in self.movies:
            if movie.title.lower() == title.lower():
                return movie
        return None

    def delete_movie(self,title):
        for movie in self.movies:
            if movie.title.lower() == title.lower():
                self.movies.remove(movie)
                return True
        return False

def main():
    database = Movie_database()
    while True:
        print("  WELCOME TO THE MOVIE DATABASE ")
        print("1. Add a new movie ")
        print("2. View all movies ")
        print("3. Search for a movie by title ")
        print("4. Delete a movie by title ")
        print("5. Exit ")

        choice = input("Choose an option : ")
        if choice == "1":
            title = input("Enter movie title : ")
            director = input("Enter movie director : ")
            year = input("Enter movie year : ")
            rating = input("Enter movie rating : ")
            movie = Movie(title,director,year,rating)
            database.add_movie(movie)
            print("MOVIE ADDED SUCCESSFULLY")
        elif choice == "2":
            movies = database.view_movie()
            if not movies:
                print("No Movies in database \n")
            else:
                for movie in movies:
                    print(movie)
                print()
        elif choice == "3":
            title = input("Enter movie title for search : ")
            movie = database.search_movie(title)
            if movie:
                print(f"Movie found : {movie}\n")
            else:
                print("Movie not found.\n")
        elif choice == "4":
            movie = database.delete_movie(title)
            if movie:
                print(f"Movie Removed {movie}\n")
            else:
                print("Movie not found.\n ")
        elif choice == "5":
            print("Exiting program, Good Bye!")
            break
        else:
            print("Invalid Option, Please tru again.\n")

if __name__ == "__main__":
    main()