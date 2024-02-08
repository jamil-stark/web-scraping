from bs4 import BeautifulSoup

with open('index.html', 'r') as html_file:
    content = html_file.read()

    soup = BeautifulSoup(content, 'lxml')
    library_titles = soup.find_all('div', class_='col-md-6')
    for library_title in library_titles:
        print(str(library_title.div.div.h5) + '\n\n\n\n')