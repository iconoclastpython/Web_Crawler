#!/usr/bin/env python
import requests

DOWNLOAD_URL = 'https://movie.douban.com/top250'

def download_page(url):
#  headers = {
#    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.80 Safari/537.36'
#  }
  data = requests.get(url)
  print data.json()

#def parse_html(html):
#  movie_list = []
#  soup = BeautifulSoup(html)
#  movie_list = soup.find('ol', attrs={'class': 'grid_view'})
#  for movie in movie_list.find_all('li'):
#    detail = movie.find('div', attrs={'class': 'hd'})
#    movie_name = detail.find('span', attrs={'class': 'title'}).getText()
#    movie_list.append(movie_name)
#    print movie_name
#
#  next_page = soup.find('span', attrs={'class': 'next'}).find('a')
#  if next_page:
#    return movie_list, DOWNLOAD_URL + next_page['href']
#  return movie_list, None


def main():
  url = DOWNLOAD_URL
  download_page(url)

if __name__ == '__main__':
  main()
