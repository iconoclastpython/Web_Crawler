#!/usr/bin/env python
'''
Basic web crawler to grasp article tiles and post timestamps

Modify Strategy:
1. Multi-Process crawler;
2. User-Agent plan;
3. Store data in MongoDB;
4. Login with authentication;
5. Reference...
'''

from bs4 import BeautifulSoup
import requests

DOWNLOAD_URL = 'https://techcrunch.com'
page = 1

def download_page(url):
  # 1. Modify U-A more powerful here 
  headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.80 Safari/537.36'}
  page = requests.get(url).content
  # 2. Get JSON file if neccessary
  return page

def parse_html(url, page):
  print "-----------------"
  print "Page: %d"%page
  page = download_page(url)
  soup = BeautifulSoup(page)
  soup_list = soup.find('ul', attrs={'class': 'river lc-padding', 'id': 'river1'})
  for article_list in soup_list.find_all('li'):
    for article in article_list.find_all('h2'):
      block = article.find('a')
      title = block.getText()
      print title

      sub_link = block.get('href')
      sub_page = download_page(sub_link)
      sub_soup = BeautifulSoup(sub_page)
      target = sub_soup.find('div', attrs={'class': 'byline'})
      try:
        detail = "Timestamp: " + target.find('time').get('datetime')
      except:
        pass
      print detail
      print '\n'

  soup_next = soup.find('div', attrs={'class': 'river-end'}).find_all('a')
  for next_url in soup_next:
    if next_url.getText() == 'Next':
      return DOWNLOAD_URL + next_url.get('href')

def main():
  url = DOWNLOAD_URL
  cur_page = page
  page_limit = 5
  while url and page_limit >= cur_page:
    url = parse_html(url, cur_page)
    cur_page += 1

if __name__ =='__main__':
  main()
