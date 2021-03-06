#!/Library/Frameworks/Python.framework/Versions/3.6/bin/python3.6
#!/usr/bin env python
# -*- coding: utf-8 -*-

import psycopg2
import datetime
import time
from lxml import html
import requests

page = requests.get('https://twitter.com/emmanuelmacron')
tree = html.fromstring(page.content)
followers_list = tree.xpath('//*[@id="page-container"]/div[1]/div/div[2]/div/div/div[2]/div/div/ul/li[3]/a/span[3]/text()')
followers_number=''.join(followers_list)

ts=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
conn = psycopg2.connect(database="twitter_followers", user="postgres", password="yusi8me")
print("Opened twitter_followers database successfully")
cur = conn.cursor()

try:
    cur.execute("CREATE TABLE followers(Dateheure TIMESTAMP, followers_number VARCHAR(5))")
except psycopg2.ProgrammingError:
    print("Table already exists")
except:
    print("Unexpected error")
    raise


if conn:
    for i in range(86400):
         conn.rollback()
         cur = conn.cursor()
         cur.execute("INSERT INTO followers VALUES (%s, %s);", (ts, followers_number))
         print('Table updated')
         conn.commit()
         time.sleep(3600)
    conn.close()
