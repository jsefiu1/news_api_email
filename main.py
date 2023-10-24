import requests
from send_email import send_email

topic = "tesla"

api_key = "c1c718a3a1d34277966889b9df18cf7a"
url = "https://newsapi.org/v2/everything?" \
    f"q={topic}&" \
    "sortBy=publishedAt&" \
    f"apiKey=c1c718a3a1d34277966889b9df18cf7a&" \
    "language=en"

# Make a request
request = requests.get(url)

content = request.json()

body = "Subject: Todays News\n\n"  # Set the subject header here

for article in content["articles"][:20]:
    if article["title"] is not None and article["description"] is not None:
        body += article["title"] + "\n" + article["description"] + "\n" + article["url"] + "\n\n"

body = body.encode("utf-8")
send_email(message=body)
# &from=2023-09-24&