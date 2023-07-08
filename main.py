import requests
from bs4 import BeautifulSoup
import json
import codecs
#https://quotes.toscrape.com/page/10/

def  search(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    for i in range(2):
            all_qoute=soup.find("div",class_='quote')
            qoute=all_qoute.find('span')
            tags=all_qoute.find_all('a',class_='tag')
            tag_texts = [tag.text for tag in tags]
            autor=all_qoute.find('small')
            data={"tags":tag_texts,
                  "author":autor.text,
                  "quote":qoute.text}
            with open('json/quotes.json', 'w') as file:
                json.dump(data, file)
                
    return None

if __name__=='__main__':
    for i in range(1,2):
        url=f'https://quotes.toscrape.com/page/{i}/'
        search(url)