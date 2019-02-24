import requests
from bs4 import BeautifulSoup

def import_content():
  res = requests.get("https://viralpatel.blog")
  soup = BeautifulSoup(res.text, "lxml")
  print(soup.select('title'))

import_content()
