import requests
res=requests.get("https://en.wikipedia.org/wiki/Virat_Kohli#Early_life")
import bs4
soup=bs4.BeautifulSoup(res.text,'lxml')
for item in soup.select('.vector-toc-text'):
    print(item.text)