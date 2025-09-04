from datetime import datetime
from PIL import Image
import requests
from io import BytesIO
import random
import textwrap
import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv('API_KEY')
# ---------------------
# FUNCTIONS
# ---------------------
def grab_movie_by_id(movie_id):
    """Fetch the main movie data."""
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={API_KEY}"
    data = requests.get(url).json()
    return data


def grab_movie_backdrops(movie_id):
    """Fetch all backdrops for the movie."""
    url = f"https://api.themoviedb.org/3/movie/{movie_id}/images?api_key={API_KEY}"
    data = requests.get(url).json()
    return data.get("backdrops", [])


def print_movie(data):
    """Print info and show a random backdrop using Pillow."""
    if "status_code" in data:
        print(f"Error {data['status_code']}: {data.get('status_message')}")
        return

    wrapper = textwrap.TextWrapper(width=80)  # wrap text at 80 characters
    genres = data.get("genres", [])
    genre_names = [genre["name"] for genre in genres]
    date_string = data.get("release_date")
    date_obj = datetime.strptime(date_string, "%Y-%m-%d")

    print("Title:", data.get("title"))

    tagline = data.get("tagline", "")
    if tagline:
        print("Tagline:"), print(wrapper.fill(tagline))  # wrapped text

    overview = data.get("overview", "")
    if overview:
        print("Overview:"), print(wrapper.fill(overview))  # wrapped text

    print("Genres:", genre_names)
    print("Release Date:", date_obj.strftime("%B %d, %Y"))
    print("Runtime:", data.get("runtime"), "Mins")

    # Fetch all backdrops
    backdrops = grab_movie_backdrops(data["id"])
    if backdrops:
        selected = random.choice(backdrops)
        image_url = "https://image.tmdb.org/t/p/w500" + selected["file_path"]

        response = requests.get(image_url)
        img = Image.open(BytesIO(response.content))
        img.show()  # opens in default image viewer (Preview on Mac)
    else:
        print("No backdrops available for this movie.")


# ---------------------
# MAIN LOOP
# ---------------------
if __name__ == "__main__":
    while True:
        user_input = input("Enter Movie ID or type 'Exit' to quit: ").strip()

        if user_input.lower() == "exit":
            print("Exiting program.")
            break

        try:
            movie_id = int(user_input)
            print("Fetching Movie Details...")
            print("-----------------=Your Result=-----------------")
            data = grab_movie_by_id(movie_id)
            print_movie(data)
        except ValueError:
            print("Invalid Movie ID. Please enter a number or 'Exit'.")
