import requests
res=requests.get("https://onepiece.fandom.com/wiki/Portgas_D._Ace")
import bs4
soup=bs4.BeautifulSoup(res.text,'lxml')
print(soup.select('.pi-image-thumbnail')[0]['src'])    #soup.select(this thing will be inspect on image)
                   
#this ''img gives all the images present so its better to use'.tumimage' instade of 'img'

#computer=soup.select('.thumbimage')
#imag=computer[0]
#im=imag['src']
#print(im)