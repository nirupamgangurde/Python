import requests
import json
query = input("What type of news are you interested in? ")
url = f"https://newsapi.org/v2/everything?q={query}&from=2024-06-12&sortBy=publishedAt&apiKey=a7ea7d79e9ff460c8a49d0788c6eef04"
r = requests.get(url)
news = json.loads(r.text)

if "articles" in news:
    for article in news["articles"]:
        print(article["title"])
        print(article["description"])
        print("-------------------------------------------------------")
else:
    print("No articles found.")
