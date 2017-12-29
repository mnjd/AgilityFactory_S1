import psycopg2
import datetime
from lxml import html
import requests

page = requests.get('https://twitter.com/emmanuelmacron')
tree = html.fromstring(page.content)
followers_list = tree.xpath('//*[@id="page-container"]/div[1]/div/div[2]/div/div/div[2]/div/div/ul/li[3]/a/span[3]/text()')
followers_number='text'
followers_number=followers_list[0]

ts=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

try:

    conn = psycopg2.connect(database="twitter_followers", user="postgres", password="yusi8me")
    print("Opened twitter_followers Database Successfully")
    cur = conn.cursor()
    cur.execute("CREATE TABLE followers(Dateheure TIMESTAMP, followers_number VARCHAR(5))")
    cur.execute("INSERT INTO followers VALUES (%s, %s);", (ts, followers_number))

    conn.commit()

#except psycopg2.DatabaseError, e:
#    
#    if con:
#        con.rollback()
#    
#    print 'Error %s' % e    
#    sys.exit(1)

finally:
    
    if conn:
        conn.close()

print("Table created")
