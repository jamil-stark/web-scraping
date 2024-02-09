from bs4 import BeautifulSoup

with open('index.html', 'r') as html_file:
    content = html_file.read()

    soup = BeautifulSoup(content, 'lxml')
    card_bodies = soup.find_all('div', class_='card-body')
    for card_body in card_bodies:
        print(card_body.h5.text)
        print(card_body.p.text)
        print()