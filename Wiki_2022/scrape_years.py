import pandas as pd
from urllib.parse import quote, unquote
import pywikibot
from itertools import islice
from time import time
from bs4 import BeautifulSoup
import requests
from tqdm import tqdm
from  scrape import get_links, get_titles, title_from_link
import os



if __name__ == "__main__":
    st = time()
    articles = get_titles()
    # print(articles.head(2))
    site = pywikibot.Site("en", "wikipedia")
    articles_set = set(articles.article.values)
    pg = pywikibot.Page(site, "%C3%81ed%C3%A1n_mac_Gabr%C3%A1in")
    x = (pg.revisions(content=True, total=1, starttime="2011-01-01T00:00:00Z", endtime="2011-12-31T00:00:00Z", reverse=True))
    # print(next(x).revid)
    for article in tqdm(articles["article"]):
        cur_links = [] # list of tuples (source, target) for current year and current article
        title = (unquote(article))
        # print(title, article)
        base_url = "https://en.wikipedia.org/w/index.php?"
        url = base_url + title
        page = pywikibot.Page(site, article)
        prev_arts = page.revisions(content=True, total=1, starttime="2009-12-31T00:00:00Z", reverse=False)
        assert(prev_arts != None)
        prev_art = next(prev_arts)
        # print(prev_art.timestamp)
        for year in range(2010, 2022):
            page = pywikibot.Page(site, article)
            try:
                revs = page.revisions(content=True, total=1, starttime=str(year)+"-01-01T00:00:00Z", endtime=str(year)+"-12-31T00:00:00Z", reverse=True)
            except:
                rev = prev_art
            else:
                prev = revs
                rev = next(revs)
            old_id = rev.revid
            urls = url + "&oldid=" + str(old_id)
            page = requests.get(urls)
            soup = BeautifulSoup(page.content, "html.parser")
            outgoing_links = get_links(soup, articles_set) # order of links seems to be completely random
            for ol in outgoing_links:
                cur_links.append((article, ol))
            # print(len(cur_links))
            links = pd.DataFrame(cur_links, columns=['linkSource', 'linkTarget'])
            output_path = "Wiki_Revs/links"+str(year)[-2:]+".tsv"
            links.to_csv(output_path, sep="\t", index=False, mode='a', header=not os.path.exists(output_path))
    en = time()
    print(en-st)
