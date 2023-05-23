import requests

# Get user input for the name
name = input("Enter the name of the anime or manga: ")

# Here we define our query as a multi-line string
query = '''
query ($search: String) {
  Media (search: $search, type: ANIME, isAdult: false) {
    id
    title {
      romaji
      english
      native
    }
  }
}
'''

# Define our query variables and values that will be used in the query request
variables = {
    'search': name
}

url = 'https://graphql.anilist.co'

# Make the HTTP API request
response = requests.post(url, json={'query': query, 'variables': variables})

# Check if the request was successful
if response.status_code == 200:
    data = response.json()

    # Extract the anime and manga data from the response
    media_list = data['data']['Media']

    # Check if there are any results
    if media_list:
        print("Matching anime and manga:")
        title = media_list['title']
        romaji = title['romaji']
        english = title['english']
        native = title['native']
        print("- Romaji: " + romaji)
        if english:
            print("  English: " + english)
        if native:
            print("  Native: " + native)
    else:
        print("No matching anime or manga found.")
else:
    print("Error occurred:", response.text)
