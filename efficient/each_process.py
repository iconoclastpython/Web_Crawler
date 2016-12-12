#!/usr/bin/env python
from bs4 import BeautifulSoup
import requests
import time, sys, Queue
from multiprocessing.managers import BaseManager

class QueueManager(BaseManager): pass

QueueManager.register('get_task_queue')
QueueManager.register('get_result_queue')

m = QueueManager(address=('127.0.0.1', 9999), authkey='crawler')
m.connect()
task = m.get_task_queue()
result = m.get_result_queue()

while True:
  page = task.get(timeout=10)
  crawl(page)
  result.put(page)

print('worker exit')
