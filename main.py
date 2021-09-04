import requests
from bs4 import BeautifulSoup



#source link where we get the articles
link = "https://www.kommersant.ru/rubric/"

#list of 'rubric' types
number = [2,3,4,5,6,7,8,9]
for num in number:
    number = num
    response = requests.get(f'{link}{number}/').text
    soup = BeautifulSoup(response, 'lxml')
    get_layoyt = soup.find('div', class_ = 'grid_cell grid_cell_big js-middle')
    get_article = get_layoyt.find('div', class_  = 'b-indetail')
    get_all = get_article.find_all('div', class_  = 'indetail__item')

#printins the article links ())
    for article in get_all:
        get_link = article.find('a').get('href')
        print(f'https://www.kommersant.ru/{get_link}')




