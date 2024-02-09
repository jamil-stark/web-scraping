from bs4 import BeautifulSoup
import requests
# import pandas as pd

url = 'https://pearldigest.com/postal-codes-list-of-all-zip-or-postal-codes-in-uganda/'
html_text = requests.get(url).text
soup = BeautifulSoup(html_text, 'lxml')
figures = soup.find_all('figure', class_='wp-block-table')
for figure in figures:
    rows = figure.find_all('tr')
    for row in rows:
        data = row.find_all('td')
        for i in data:
            # print with tab space
            print(i.text, end='\t')
        print()
        