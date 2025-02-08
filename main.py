import requests

api_key = "3762647bc9f2433c94b8e902dbcbfc74"
url = ("https://newsapi.org/v2/everything?q=tesla&"
       "from=2025-01-08&sortBy=publishedAt&apiKey="
       "3762647bc9f2433c94b8e902dbcbfc74")

# Make request
request = requests.get(url)

# Get a dictionary with data
content = request.json()

# Access the article titles and description
for article in content["articles"]:
    print(article["title"])
    print(article["description"])
