from PIL import Image
import requests
from io import BytesIO
from datetime import datetime
import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv('API_KEY')
def grab_movie_by_id(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={API_KEY}"
    data = requests.get(url).json()
    return data



def print_movie(data):
    if "status_code" in data:
        print(f"Error {data['status_code']}: {data.get('status_message')}")
    else:
        genres = data.get("genres", [])
        date_string = data.get("release_date")
        date_obj = datetime.strptime(date_string, "%Y-%m-%d")
        genre_names = [genre["name"] for genre in genres]
        print("Title:", data.get("title"))
        print("Genres:" , genre_names)
        print(date_obj.strftime("%B %d, %Y"))
        image_url = "https://image.tmdb.org/t/p/w500" + data.get("backdrop_path")
        response = requests.get(image_url)
        img = Image.open(BytesIO(response.content))
        img.show()  # opens the image in the default image viewer
''

