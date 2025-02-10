import requests
from send_email import send_email

category = "business"

api_key = "3762647bc9f2433c94b8e902dbcbfc74"
url = ("https://newsapi.org/v2/top-headlines?"
       "country=us&"
       f"category={category}&"
       "apiKey=3762647bc9f2433c94b8e902dbcbfc74")

# Make request
request = requests.get(url)

# Get a dictionary with data
content = request.json()

# Access the article titles and description
body = ""
for article in content["articles"][:20]:
    if article["content"] is not None:
        body =  (body + article["title"] + "\n"
                + article["description"] + "\n"
                + article["url"] + 2*"\n")

body = "Subject: News" + "\n" + body
body = body.encode("utf-8")
send_email(message=body)