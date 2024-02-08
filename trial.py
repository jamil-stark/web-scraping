import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

url = "https://www.imdb.com/chart/top"
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

movies = []