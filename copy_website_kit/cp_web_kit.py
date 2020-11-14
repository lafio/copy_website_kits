import requests,re
from bs4 import BeautifulSoup

def func(url):
    html = requests.get(url)
    soup = BeautifulSoup(html.text,'lxml')#.select('.pmbt')

    list=[]
    for tag in soup.find_all("div",class_="pmbt"):
        if tag.text not in list:
            list.append(tag.text.replace('Â',''))
        #print(tag.text)

    for tag in soup.find_all("div",class_="pmxbt"):
        if tag.text not in list:
            list.append(tag.text.replace('Â',''))

    for tag in soup.find("div",class_="pdright").find_all("span"):
            if tag.text not in list:
                list.append(tag.text.replace('Â',''))
    for i in list:
        print(i)

if __name__ == "__main__":

    url = 'https://www.cobetterfiltration.com/cobetter/456/'
    
    func(url)