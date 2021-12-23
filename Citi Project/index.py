from bs4 import BeautifulSoup
import requests

xml_links = ['http://feeds.washingtonpost.com/rss/business/technology',
'http://feeds.bbci.co.uk/news/technology/rss.xml',
'https://www.technologyreview.com/feed/',
'https://rss.nytimes.com/services/xml/rss/nyt/Technology.xml',
'https://www.forbes.com/business/feed/',
'https://www.macworld.com/feed',
'https://feeds.npr.org/1019/rss.xml',
'https://www.wired.com/feed']
link_list = []
title_list = []

for i in xml_links:
    url = requests.get(i)
    soup = BeautifulSoup(url.content, 'xml')
    items = soup.find_all('item')
    for item in items:
        title = item.title.text
        the_link = item.link.text
        link_list.append(the_link)
        title_list.append(title)

