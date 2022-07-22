from urllib import request, error
from bs4 import BeautifulSoup

l = []
with request.urlopen('http://alatoo.edu.kg/view/public/news/list.xhtml#gsc.tab=0') as resp:
    data = resp.read()
    soup = BeautifulSoup(data, 'html.parser')
    items = soup.find_all('div', attrs={'class': "text"})
    for item in items:
        text = item.get_text()
        l.append(text)
# print(l[0])