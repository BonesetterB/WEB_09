import requests
from bs4 import BeautifulSoup
import json



def  search(url, ex_author):
    exsist_autor=[]
    liist=[]
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    all_qoute=soup.find("div",class_='quote')

    qoute=all_qoute.find('a')
    new_url=f"http://quotes.toscrape.com/{qoute.get('href')}"
    response = requests.get(new_url)
    soup = BeautifulSoup(response.text, 'lxml')
    autor_page=soup.find("div",class_='author-details')
    autor=autor_page.find('h3')
    born=autor_page.find('span',class_='author-born-date')
    local_born=autor_page.find('span',class_='author-born-location')
    desk=soup.find('div',class_='author-description')

    if autor.text in exsist_autor or autor.text in ex_author:
        print(f"Автор {autor.text} існує у JSON файлі.")
    else:
        exsist_autor.append(autor.text)
        data={"fullname":autor.text,
            "born_date":born.text,
            "born_location":local_born.text,
            "description":desk.text.strip()}
        liist.append(data)
    for i in range(9):
        all_qoute=all_qoute.find_next_sibling("div",class_='quote')
        qoute=all_qoute.find('a')
        new_url=f"http://quotes.toscrape.com/{qoute.get('href')}"
        response = requests.get(new_url)
        soup = BeautifulSoup(response.text, 'lxml')
        autor_page=soup.find("div",class_='author-details')
        autor=autor_page.find('h3')
        born=autor_page.find('span',class_='author-born-date')
        local_born=autor_page.find('span',class_='author-born-location')
        desk=soup.find('div',class_='author-description')
        
        if autor.text in exsist_autor or autor.text in ex_author:
            print(f"Автор {autor.text} існує у JSON файлі.")
        else:
            exsist_autor.append(autor.text)
            data={"fullname":autor.text,
                "born_date":born.text,
                "born_location":local_born.text,
                "description":desk.text.strip()}
            liist.append(data)
                
    return liist, exsist_autor


if __name__=='__main__':
    data=[]
    lisst_exist_author=[]
    for i in range(1,11):
        url=f'https://quotes.toscrape.com/page/{i}/'
        page, list_autor=search(url,lisst_exist_author)
        data.extend(page)
        lisst_exist_author.extend(list_autor)
   
    
    with open('json/authors.json', 'w') as file:
        json.dump(data, file, indent=4,  separators=(", ", ": "))
#ensure_ascii=False,