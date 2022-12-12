#making requests to the anilist api
import requests
import json
#anilist api url
url = "https://graphql.anilist.co"

#query to random manga from anilist that is romance, action and made after 2010
query = """
query ($page: Int , $genre: String ,$startDate_greater: FuzzyDateInt) {
    Page (page: $page, perPage: 1) {
        media (genre: $genre,startDate_greater :$startDate_greater, type: MANGA) {
            id
            title {
                english
            }
            coverImage {
                large
            }
            description
            genres
            startDate {
                year
                month
                day
            }
            endDate {
                year
                month
                day
            }
            chapters
            volumes
            status
            format
            siteUrl
        }
    }
}
"""
#variables for the query
variables = {
    "page": 1, "genre": "Romance" , "genre": "Action", "startDate_greater":  20160000
}
response = requests.post(url, json={'query': query, 'variables': variables})

#response in json format in a new file
with open('anilist.json', 'w') as f:
    json.dump(response.json(), f, indent=4)


