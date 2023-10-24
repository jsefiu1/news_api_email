import requests 

api_key = "c1c718a3a1d34277966889b9df18cf7a"
url = "https://newsapi.org/v2/everything?q=tesla&from=2023-09-24&sortBy=publishedAt&apiKey=c1c718a3a1d34277966889b9df18cf7a"

# Make request
request = requests.get(url)

# Get a dictionary with data
content = request.json()

# Access the article iems and description
for article in content["articles"]:
    print(article["title"])
    print(article["description"])