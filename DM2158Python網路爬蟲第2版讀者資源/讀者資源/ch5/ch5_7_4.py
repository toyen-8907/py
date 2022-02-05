# ch5_7_4.py
import bs4

response = "<h1 class='boldtext'>深智數位</h1>"
objSoup = bs4.BeautifulSoup(response, 'lxml')
tag = objSoup.find('h1', class_='boldtext')
print(tag)
print(tag.text)
print('-'*70)
tag = objSoup.find('h1', 'boldtext')
print(tag)
print(tag.text)













