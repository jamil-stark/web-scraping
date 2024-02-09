from bs4 import BeautifulSoup
import requests
import pandas as pd

url = 'https://pearldigest.com/postal-codes-list-of-all-zip-or-postal-codes-in-uganda/'
html_text = requests.get(url).text
soup = BeautifulSoup(html_text, 'lxml')
figures = soup.find_all('figure', class_='wp-block-table')

table_data = []

for figure in figures:
    rows = figure.find_all('tr')
    for row in rows:
        data = [cell.get_text(strip=True) for cell in row.find_all('td')]
        table_data.append(data)

df = pd.DataFrame(table_data)
excel_file_path = 'postal_codes_uganda.xlsx'
df.to_excel(excel_file_path, index=False)

print(f"Data has been saved to '{excel_file_path}'")
