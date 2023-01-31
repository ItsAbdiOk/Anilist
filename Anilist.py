import pandas as pd
import json
import requests

#anilist api url
url = "https://graphql.anilist.co"

#query to random manga from anilist that is romance, action and made after 2010
query = """
query ($page: Int , $genre_in: [String] ,$startDate_greater: FuzzyDateInt, $sort: MediaSort , $popularity: Int) {
    Page (page: $page, perPage: 1) {
        media (genre_in: $genre_in,startDate_greater :$startDate_greater,sort:$sort, popularity :$popularity ,type: MANGA) {
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
def UserInput():
    genre_string = input("Enter a list of genres, separated by commas: ")
    genre_list = genre_string.split(",")
    
    # Next, make each genre have a capital first letter
    capitalized_genre_list = []
    for genre in genre_list:
        capitalized_genre = genre[0].upper() + genre[1:]    
        capitalized_genre_list.append(capitalized_genre)
    # Validate the entered genres
    # You can use the AniList API to get the list of available genres
    # and check if the entered genres exist in that list
    
    return capitalized_genre_list


# Get the list of genres entered by the user
List = ["Romance", "Action", "Comedy"]
variables = {
    "page": 1, 
    "genre_in": List ,
    "sort": "popularity",
    "startDate_greater":  20160000,
    "type": "MANGA"
}

# Make the request to the AniList API
response = requests.post(url, json={'query': query, 'variables': variables})

# Parse the response text as JSON
response_json = response.json()

print (response_json)
