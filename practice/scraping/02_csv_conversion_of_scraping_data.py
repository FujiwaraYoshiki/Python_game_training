import requests
from bs4 import BeautifulSoup
import pandas as pd

# Retrieve topic information titles and articles from news sites and compile them into a csv.

# URL list for scraping
urls = [
    "https://news.yahoo.co.jp/",
    # Add pages as needed
]

# Articles title & link List
titles = []
links = []

for url in urls:

    response = requests.get(url)
    response.encoding = response.apparent_encoding

    soup = BeautifulSoup(response.text, "html.parser")

    for article in soup.find_all("li", class_="sc-1nhdoj2-0"):
        title = article.get_text()
        link = article.find("a")["href"]
        titles.append(title)
        links.append(link)

df = pd.DataFrame({
    "Title": titles,
    "Link": links
})

df.to_csv('articles_data/articles.csv', index=False, encoding='utf-8-sig')

print("Scraping is now complete.Article titles and links have been saved to articles.csv.!")
