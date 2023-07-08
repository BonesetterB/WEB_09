import requests
from bs4 import BeautifulSoup
import json

def  search(url):
    liist=[]
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    all_qoute=soup.find("div",class_='quote')
    qoute=all_qoute.find('span')
    tags=all_qoute.find_all('a',class_='tag')
    tag_texts = [tag.text for tag in tags]
    fixed_quote = qoute.text.replace("\u201c", '').replace("\u201d", '')
    autor=all_qoute.find('small')
    data={"tags":tag_texts,
        "author":autor.text,
        "quote":fixed_quote}
    liist.append(data)
    for i in range(9):
        all_qoute=all_qoute.find_next_sibling("div",class_='quote')
        qoute=all_qoute.find('span')
        tags=all_qoute.find_all('a',class_='tag')
        tag_texts = [tag.text for tag in tags]
        fixed_quote = qoute.text.replace("\u201c", '').replace("\u201d", '')
        autor=all_qoute.find('small')
        data={"tags":tag_texts,
            "author":autor.text,
            "quote":fixed_quote}
        liist.append(data)
                
    return liist

if __name__=='__main__':
    data=[]
    for i in range(1,11):
        url=f'https://quotes.toscrape.com/page/{i}/'
        page=search(url)
        data.extend(page)

    
    with open('json/quotes.json', 'w') as file:
        json.dump(data, file, indent=4, separators=(", ", ": "))