import pandas as pd
from urllib.parse import quote, unquote
import pywikibot
from itertools import islice
from time import time
from bs4 import BeautifulSoup
import requests
from  scrape import get_links, get_titles
from urllib.parse import quote, unquote

site = pywikibot.Site("en", "wikipedia")
title = unquote("Functional_programming")
page = pywikibot.Page(site, title)
year = 2018
revs = page.revisions(content=True, total=1, starttime=str(year)+"-01-01T00:00:00Z", endtime=str(year)+"-12-31T00:00:00Z", reverse=True)
rev = next(revs)
print(rev.timestamp)
old_id = rev.revid
base_url = "https://en.wikipedia.org/w/index.php?"
url = base_url + title
urls = url + "&oldid=" + str(old_id)
print(urls)
page = requests.get(urls)
soup = BeautifulSoup(page.content, "html.parser")
articles = get_titles()
articles_set = set(articles.article.values)
outgoing_links = get_links(soup, articles_set) # order of links seems to be completely random
print(len(outgoing_links))
