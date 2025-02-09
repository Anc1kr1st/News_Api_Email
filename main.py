import requests
from send_email import send_email

topic = "tesla"

api_key = "3762647bc9f2433c94b8e902dbcbfc74"
url = ("https://newsapi.org/v2/everything?"
       f"q={topic}&"
       "from=2025-01-09&"
       "sortBy=publishedAt&"
       "apiKey=3762647bc9f2433c94b8e902dbcbfc74&language=en")

# Make request
request = requests.get(url)

# Get a dictionary with data
content = request.json()

# Access the article titles and description
body = ""
for article in content["articles"][:20]:
    if article["title"] is not None:
        body = "Subject: Today's new" \
                + "\n" + body + article["title"] + "\n" \
                + article["description"] + "\n" \
                + article["url"] + 2*"\n"

body = body.encode("utf-8")
send_email(message=body)