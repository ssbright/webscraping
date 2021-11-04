import requests
from bs4 import BeautifulSoup
import pprint

res = requests.get('https://news.ycombinator.com/news') #Like a browser, requsting access to url html
res2 = requests.get('https://news.ycombinator.com/news?p=2') #Like a browser, requsting access to url html
soup = BeautifulSoup(res.text, 'html.parser')
soup2 = BeautifulSoup(res2.text, 'html.parser')
subtext = soup.select('.subtext')
subtext2 = soup2.select('.subtext')
links = soup.select('.titlelink')
links2 = soup2.select('.titlelink')

mega_links = links + links2
mega_subtext = subtext + subtext2

def sort_storeis_by_votes(hnlist):
  return sorted(hnlist, key= lambda k:k['votes'], reverse=True)

def creare_custom_hn(links, subtext):
  hn=[]
  for idx, item in enumerate(links):
    title = item.getText()
    href = item.get('href', None)
    vote = subtext[idx].select('.score')
    if len(vote):
      points = int(vote[0].getText().replace(' points', ''))
      #print(points)
      if points > 99:
        hn.append({'title': title, 'link': href, 'votes': points})
  return sort_storeis_by_votes(hn)

pprint.pprint(creare_custom_hn(mega_links, mega_subtext))
