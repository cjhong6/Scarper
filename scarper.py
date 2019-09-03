from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('https://treehouse-projects.github.io/horse-land/index.html')
soup = BeautifulSoup(html.read(), 'html.parser')

#get the div tag -> class=featured -> h2 -> text
# feature_header = soup.find('div',{'class':'featured'}).h2
# print(feature_header.get_text())

#search for specific css class use attrs
# for button in soup.find(class_ = 'button button--primary'):
#   print(button)

for link in soup.find_all('a'):
  print(link.get('href'))