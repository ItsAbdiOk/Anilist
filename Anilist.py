# Import the pandas library
import pandas as pd
# Import the JSON library
import json
#making requests to the anilist api
import requests

#anilist api url
url = "https://graphql.anilist.co"

#query to random manga from anilist that is romance, action and made after 2010
query = """
query ($page: Int , $genre_in: [String] ,$startDate_greater: FuzzyDateInt) {
    Page (page: $page, perPage: 1) {
        media (genre_in: $genre_in,startDate_greater :$startDate_greater, type: MANGA) {
            id
            title {
                english
                romaji
            }
            genres
        }
    }
}
"""
# First, get the user input and split it into a list of genres
genre_string = input("Enter a list of genres, separated by commas: ")
def UserInput(genre_string):
    genre_list = genre_string.split(",")
    # Next, make each genre have a capital first letter
    capitalized_genre_list = []
    for genre in genre_list:
        capitalized_genre = genre[0].upper() + genre[1:]
        capitalized_genre_list.append(capitalized_genre)
    return capitalized_genre_list



List = UserInput(genre_string)
variables = {
    "page": 1, "genre_in": List , "startDate_greater":  20160000
}
response = requests.post(url, json={'query': query, 'variables': variables})

# parse the response text as JSON
response_json = response.json()

# get the media object from the response
media = response_json['data']['Page']['media'][0]

# get the romaji title from the media object
title = media['title']['romaji']
Genres = media['genres']
# print the title
print(title)
print(Genres)
