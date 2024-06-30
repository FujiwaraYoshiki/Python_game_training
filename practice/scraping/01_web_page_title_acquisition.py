import requests
from bs4 import BeautifulSoup
# URL of the website to be retrieved
url = "https://www.coca-cola.com/jp/ja/brands/chillout"

# Get web page content
response = requests.get(url)

# Set encoding (specify appropriate encoding)
response.encoding = response.apparent_encoding

# Parsing HTML
soup = BeautifulSoup(response.text, "html.parser")

# Get Title
title = soup.title.string
print("Web page title is", title)
