from ApiHandler import *

while True:
    try:
        movie_id: int = int(input("Enter Movie ID: "))
        data = grab_movie_by_id(movie_id)
        print("Fetching Movie Details...")
        print("-----------------=Your Result is=-----------------")
        print_movie(data)
        break  # exit loop if everything works
    except (ValueError, TypeError):
        print("Invalid Movie ID. Please try again.")
