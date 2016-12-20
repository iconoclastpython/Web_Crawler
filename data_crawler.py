#!/usr/bin/env python

'''
Basic web crawler to grasp article tiles and post timestamps

Modify Strategy:
1. Queue management;
2. Multi-Process crawler;
3. User-Agent plan;
4. Store data in MongoDB;
5. Login with authentication;
6. Anti-Crawler procedures;
7. Docker;
8. Reference...

Packages:
*** brew ***
1. rabbitmq;

*** pip ***
1. BeautifulSoup;
2. pika;

'''


from bs4 import BeautifulSoup
import requests

from multiprocessing import Pool
from multiprocessing import Process

import time


DOWNLOAD_URL = 'https://techcrunch.com'
urls = [DOWNLOAD_URL]

def download_page(url):
  # 1. Modify U-A more powerful here 
  headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.80 Safari/537.36'}
  page = requests.get(url).content
  # 2. Get JSON file if neccessary
  return page

def groom_url(url):
  page = download_page(url)
  soup = BeautifulSoup(page)
  soup_next = soup.find('div', attrs={'class': 'river-end'}).find_all('a')
  for next_url in soup_next:
    if next_url.getText() == 'Next':
      urls.append(DOWNLOAD_URL + next_url.get('href'))
      print 'Get url: %s'%DOWNLOAD_URL + next_url.get('href') 
      return DOWNLOAD_URL + next_url.get('href')

def parse_html(url):
  print "-----------------"
  print "Page: %s"%url
  page = download_page(url)
  soup = BeautifulSoup(page)
  soup_list = soup.find('ul', attrs={'class': 'river lc-padding', 'id': 'river1'})
  for article_list in soup_list.find_all('li'):
    for article in article_list.find_all('h2'):
      block = article.find('a')
      title = block.getText()
      print url, "-->", title

      sub_link = block.get('href')
      sub_page = download_page(sub_link)
      sub_soup = BeautifulSoup(sub_page)
      target = sub_soup.find('div', attrs={'class': 'byline'})
      try:
        detail = "Timestamp: " + target.find('time').get('datetime')
      except:
        pass
      print url, "-->", detail
      print '\n'


def main():
  # Get all urls
  cur_page = 1
  page_limit = 10
  index = 0
  while page_limit > cur_page:
    groom_url(urls[index])
    index += 1
    cur_page += 1
  print "url list: ", urls

  # Multi-Process crawler
  start_time = time.time()
  pool = Pool(10)
  pool.map(parse_html, urls)
  pool.close()
  pool.join()

  print time.time() - start_time

  # Here disorder print should be save with keys in database
  # Better to save url or html content in an advanced queue, but avoid OOM

if __name__ =='__main__':
  main()
