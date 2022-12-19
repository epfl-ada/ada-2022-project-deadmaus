import pandas as pd
from urllib.parse import quote, unquote
import pywikibot
from itertools import islice
from time import time, sleep
from bs4 import BeautifulSoup
import requests
from tqdm import tqdm
from  scrape import get_links, get_titles, title_from_link
import os
import multiprocessing
from functools import partial

def get_rev_links(article, articles_set, articles_seen):
    if article in articles_seen:
        return None
    site = pywikibot.Site("en", "wikipedia")
    links09 = pd.read_csv('wikispeedia_paths-and-graph/links.tsv', comment='#', delimiter='\t', names=['linkSource', 'linkTarget'])
    title = (unquote(article))
    prev_links = list(links09[links09["linkSource"] == article].itertuples(index=False, name=None)) # link structure from the wikispeedia dataset
    base_url = "https://en.wikipedia.org/w/index.php?"
    url = base_url + title
    pg = pywikibot.Page(site, article)
    res = dict()
    for year in range(2010, 2022):
        cur_links = [] # list of tuples (source, target) for current year and current article
        try:
            t1 = time()
            revs = pg.revisions(content=True, total=1, starttime=str(year)+"-01-01T00:00:00Z", endtime=str(year)+"-12-31T00:00:00Z", reverse=True)
            rev = next(revs)
            t2 = time()
        except:
            cur_links = prev_links
        else:
            num += 1
            prev = revs
            old_id = rev.revid
            urls = url + "&oldid=" + str(old_id)
            try:
                r_st = time()
                page = requests.get(urls, timeout=20)
                r_en = time()
            except:
                print("Incomplete")
                print(article, year)
                coll = False
                break
            else:
                bs_st = time()
                soup = BeautifulSoup(page.content, "html.parser")
                bs_en = time()
                ln_st = time()
                outgoing_links = get_links(soup, articles_set) # order of links seems to be completely random
                for ol in outgoing_links:
                    cur_links.append((article, ol))
                ln_en = time()
                prev_links = cur_links

            res[year] = cur_links

    return res

if __name__ == "__main__":
    pool = multiprocessing.Pool(16)
    articles = get_titles().article.to_list()
    articles_set = set(articles)
    articles = articles[:1]
    links10 = pd.read_csv('Wiki_Revs/links10.tsv', comment='#', delimiter='\t', names=['linkSource', 'linkTarget'])
    articles_seen = set(links10.linkSource.values)
    for links in tqdm(pool.imap_unordered(partial(get_rev_links, articles_set=articles_set, articles_seen=articles_seen), articles)):
        if links:
            for year in range(2010, 2022):
                output_path = "Wiki_Revs/links"+str(year)[-2:]+".tsv"
                links.to_csv(output_path, sep="\t", index=False, mode='a', header=not os.path.exists(output_path))
        else:
            print("Success")