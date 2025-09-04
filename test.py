import os
from dotenv import load_dotenv


import csv


load_dotenv()
API_KEY = os.getenv('API_KEY')

with open('personal_favorites.csv') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    header = next(reader)
    for row in reader:
        title = row[1]
        mov_id = row[0]



#choice = input("Pick a movie from above: ")
#if choice == row[1]:
 #   movie = row[1]
  #  print(f"your choice is {movie}")
#else:
#    print("invalid choice")




print(title)
print(mov_id)