import requests
res=requests.get("https://en.wikipedia.org/?title=Portgas_D._Ace&redirect=no ")

import bs4
soup=bs4.BeautifulSoup(res.text,'lxml')
soup.select('title')
#Notice what is returned here, its actually a list containing all the title elements (along with their tags). 
#You can use indexing or even looping to grab the elements from the list. Since this object it still a specialized tag,
#we cna use method calls to grab just the text.
tit=soup.select('title')
print(tit[0].getText())