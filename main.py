import requests
from bs4 import BeautifulSoup
import json
#https://quotes.toscrape.com/page/10/

def  search():
    url = 'http://quotes.toscrape.com'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    while True:
        try:
            all_qoute=soup.find_next_sibling("div",class_='quote')
            qoute=all_qoute.find('span')
            tags=all_qoute.find_all('a',class_='tag')
            tag_texts = [tag.text for tag in tags]
            autor=all_qoute.find('small')
            with open('data.json', 'w') as file:
                json.dump("json/quotes.json", file)
            print(qoute.text)
            print(tag_texts)
            print(autor.text)
        except:
            break
    return None

if __name__=='__main__':
    print(search())