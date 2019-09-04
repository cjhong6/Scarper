from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

links = []

def internal_links(linkURL):
  html = urlopen('https://treehouse-projects.github.io/horse-land/{}'.format(linkURL))
  soup = BeautifulSoup(html.read(), 'html.parser')
  return soup.find('a', href=re.compile('(.html)$'))

if __name__ == '__main__':
  urls = internal_links('index.html')

  while len(urls) > 0:
    link = urls.attrs['href']
    if link not in links:
      links.append(link)
      print(link)
      urls = internal_links(link)
    else:
      break
