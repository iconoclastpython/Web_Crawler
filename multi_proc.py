from multiprocessing import Pool
from multiprocessing import Process
import requests

urls = ['https://google.com', 'https://baidu.com', 'https://leetcode.com', 'https://techcrunch.com']

def getStatus(url):
  status = requests.get(url).encoding
  print url + ' ' + status
#  return status

if __name__ == '__main__':
#  for url in urls:
#    getStatus(url)

  p = Pool(4)
  p.map(getStatus, urls)

  p.close()
  p.join()
