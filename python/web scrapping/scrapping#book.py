#goal-to get title of every book with 4 star rating
#website-http://books.toscrape.com/
import requests
import bs4
base_url='http://books.toscrape.com/catalogue/page-{}.html'
book_list=[]
for n in range(1,51):
    res=requests.get(base_url.format(n))
    soup=bs4.BeautifulSoup(res.text,'lxml')
    products=soup.select(".product_pod")
    for product in products:
       if len(product.select(".star-rating.Four"))!=0:#check step by step by printing the html syntax
           book_list.append(product.select("a")[1]['title'])
print(book_list)