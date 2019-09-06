from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

internal_links = []
external_links = []

def get_internal_links(linkURL):
  html = urlopen('https://treehouse-projects.github.io/horse-land/{}'.format(linkURL))
  soup = BeautifulSoup(html.read(), 'html.parser')
  return soup.find('a', href=re.compile('(.html)$')) #end wirth .html

def recursive_link_retrieval(linkURL):
    links = list()    
    html = urlopen(linkURL)
    soup = BeautifulSoup(html, 'html.parser')

    new_links = soup.findAll('a', href=re.compile('(^https://)'))
    for link in new_links:
        if link.attrs['href'] not in links:
            links.append(link.attrs['href'])
    return links

if __name__ == '__main__':
  urls = get_internal_links('index.html')

  while len(urls) > 0:
    link = urls.attrs['href']
    if link not in internal_links:
      internal_links.append(link)
      print(link)
      urls = get_internal_links(link)
    else:
      break
  
  external_links = recursive_link_retrieval('https://treehouse-projects.github.io/horse-land/index.html')
  for link in external_links:
    print(link)

