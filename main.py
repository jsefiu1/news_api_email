import requests
from send_email import send_email

api_key = "c1c718a3a1d34277966889b9df18cf7a"
url = "https://newsapi.org/v2/everything?q=tesla&from=2023-09-24&sortBy=publishedAt&apiKey=c1c718a3a1d34277966889b9df18cf7a"

# Make a request
request = requests.get(url)

content = request.json()

body = ""

for article in content["articles"]:
    title = article.get("title", "")
    description = article.get("description", "")

    if title:
        body = body + title + "\n"

    if description:
        body = body + description + 2 * "\n"

# Encode the message as UTF-8
body = body.encode("utf-8")

send_email(message=body)


# Check if the request was successful
# if response.status_code == 200:
#     content = response.json()

#     # Create an empty message to accumulate news content  
#     raw_message = ""

#     for article in content["articles"]:
#         title = article["title"]
#         description = article["description"]
#         raw_message += f"{title}\n{description}\n\n"

#     user_email = "sefiujon@gmail.com"

#     # Send the email with the news content
#     send_email(user_email, raw_message)
# else:
#     print("Failed to retrieve news data")

