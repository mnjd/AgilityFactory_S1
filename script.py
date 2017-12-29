from lxml import html
import requests

page = requests.get('https://twitter.com/emmanuelmacron')
tree = html.fromstring(page.content)
followers_list = tree.xpath('//*[@id="page-container"]/div[1]/div/div[2]/div/div/div[2]/div/div/ul/li[3]/a/span[3]/text()')

print(followers_list)

#followers='text'
#followers=followers_list[0]
#followers=followers.replace('\xa0', ' ')

#print(followers)


